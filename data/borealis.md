# Borealis

Polytechnique Montréal has an official recommended repository for research data
called [Borealis](https://borealisdata.ca/). From their webpage:

> Borealis, the Canadian Dataverse Repository, is a bilingual,
> multidisciplinary, secure, Canadian research data repository, supported by
> academic libraries and research institutions across Canada. Borealis supports
> open discovery, management, sharing, and preservation of Canadian research
> data.

See also [the Polytechnique library website about Borealis](https://libguides.biblio.polymtl.ca/research_data/dataverse).

The Borealis webpage and API are clunky to use, but it can be a useful place to
publish a dataset related to a scientific publication.

## Admin info

Our contact at the Polytechnique library, who has admin rights for the PolyMTL
dataverse on Borealis, is [Brendan Fitzgibbon](mailto:brendan.fitzgibbon@polymtl.ca).

At NeuroPoly, [Mathieu Guay-Paquet](mailto:mathieu.guay-paquet@polymtl.ca) also
has a subset of the admin permissions.

## How to browse datasets

The entire collection can be searched from [the root dataverse](https://borealisdata.ca/dataverse/dv).

The sub-collection of datasets at Poly can be searched from [Dataverse de Polytechnique Montréal](https://borealisdata.ca/dataverse/polymtl).

The sub-sub-collection of datasets published by NeuroPoly can be searched from [Laboratoire NeuroPoly](https://borealisdata.ca/dataverse/neuropoly).

## How to download a dataset

Reference: <https://guides.dataverse.org/en/latest/api/dataaccess.html>

1. Find the dataset DOI at:
   <https://borealisdata.ca/dataverse/neuropoly>

2. Get an API token from:
   <https://borealisdata.ca/dataverseuser.xhtml?selectTab=apiTokenTab>

3. Get the dataset description JSON with the following shell commands.
   Among other things, this contains the list of all the files in the dataset.

   ```sh
   URL='https://borealisdata.ca'
   TOKEN='519b9432-ae39-4d52-831c-4453110191c6'  # example
   DOI='doi:10.5683/SP4/P9ZCIW'
   VERSION=':draft'  # or ':latest' or a specific version
   curl --location \
        --header "X-Dataverse-key: $TOKEN" \
        --header 'Accept: application/json' \
        --output 'meta.json' \
        "$URL/api/datasets/:persistentId/versions/$VERSION?persistentId=$DOI"
   ```

4. Group the files into <5GB chunks, using the following Python script.
   This is necessary because the individual file download API is slow (and
   doesn't create directories), and the bulk file download API only returns a
   subset of the files if the total size is too large.

   The input is the `meta.json` file from the previous step. The output is a
   set of files `partN.txt`. Each output file contains a comma-separated list
   of numeric file IDs, in the format accepted by the bulk file download API.

   ```py
   #!/usr/bin/env python3
   import json

   parts: list[dict[int, int]] = []  # [{fileid: filesize}]

   meta = json.loads(open('meta.json').read())
   assert isinstance(meta, dict)
   data = meta['data']
   assert isinstance(data, dict)
   files = data['files']
   assert isinstance(files, list)
   for file in files:
       assert isinstance(file, dict)
       dataFile = file['dataFile']
       assert isinstance(dataFile, dict)
       fileid = dataFile['id']
       assert isinstance(fileid, int)
       filesize = dataFile['filesize']
       assert isinstance(filesize, int)
       for part in parts:
           if filesize + sum(part.values()) <= 4<<30:
               part[fileid] = filesize
               break
       else:
           parts.append({fileid: filesize})

   for index, part in enumerate(parts):
       open(f'part{index}.txt', 'w').write(','.join(
           str(fileid) for fileid in part.keys()
       ))
   ```

5. Download all the chunks with the following shell commands.
   (Instead of a `for` loop, you can also run several downloads in parallel.)

   ```sh
   # needs URL and TOKEN, but not DOI or VERSION
   for part in part*.txt
   do curl --location \
           --header "X-Dataverse-key: $TOKEN" \
           --header 'Content-Type: text/plain' \
           --header 'Accept: application/zip' \
           --data-binary "@$part" \
           --output "${part/%txt/zip}" \
           "$URL/api/access/datafiles?format=original"
   done
   ```

6. Check the manifests for download errors with the following shell commands.
   Each line of output gives an error message for a missing file.
   If the command produces no output, everything is fine.
   (The bulk file download API adds a file called `MANIFEST.TXT` in each zip
   file with a status line for each requested file.)

   ```sh
   for part in part*.zip
   do unzip -p "$part" MANIFEST.TXT | grep -v ') [0-9]\+ bytes\.\s*$'
   done
   ```

7. Extract the actual files with the following shell commands.
   (This excludes the added `MANIFEST.TXT` file from each zip.)

   ```sh
   for part in part*.zip
   do unzip "$part" -x MANIFEST.TXT
   done
   ```

8. Remove the temporary files (the dataset description JSON, the lists of file
   IDs to download, and the downloaded zip files).

   ```sh
   rm meta.json part*.{txt,zip}
   ```

9. Revoke the API token, to prevent others from impersonating you:
   <https://borealisdata.ca/dataverseuser.xhtml?selectTab=apiTokenTab>

## How to upload a dataset

Contact [Brendan Fitzgibbon](mailto:brendan.fitzgibbon@polymtl.ca) to create
your account, give you the necessary permissions to create and upload a dataset,
and review your metadata before publication.
