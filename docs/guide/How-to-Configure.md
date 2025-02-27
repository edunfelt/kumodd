# How to Configure

## Selecting Columns for Output

The command line option, __-col normal__, selects the column set named 'normal' shown
below.  This is also the default if no __-col__ option is specified.

Below 'normal:' is a set of columns for output. The numbers are the fixed width of
columns on standard output (CSV export has no limit). The complete list of the column
sets is shown in [Default YAML Configuration File](../Default-configuration).

``` yaml
gdrive:
  column_sets:
    normal:
    - [title, 20]
    - [category, 4]
    - [status, 7]
    ...
```

Metadata has a tree structure (*see* [Example Metadata](../Example-Metadata)).  To
select values, use [jsonpath syntax](https://github.com/h2non/jsonpath-ng). For example,
in the column set below, 'owners[*].emailAddress' selects a list of the file's owner
email addresses. Numbers below are the settings of fixed widths of the columns on
standard output.

``` yaml
gdrive:
  column_sets:
    owners:
    - [status, 7]
    - ['owners[*].emailAddress', 20]
    - [fullpath, 50]
```

Column titles are specified under the column\_titles key, below.  Each item translates a
column value to a column title.  Names containing spaces or delimiters must be quoted.

``` yaml
gdrive:
  column_titles:
    status:  Status
    'owners[*].emailAddress':  Owners
    fullpath:  Full Path
    ...
```

## Metadata Names

[Example raw metadata](https://github.com/rich-murphey/kumodd/wiki/Example-Metadata) shows a variety of available metadata.
They include:

CSV Columns		| Description 
:------			| :-----------
title			| File name
category		| one of: doc, xls, ppt, text, pdf, image, audio, video or other
modifiedDate		| Last Modified Time (UTC)
lastViewedByMeDate	| Time Last Viewed by Account Holder (UTC)
md5Checksum             | MD5 digest of remote file. None if file is a native Google Apps Document.
md5Match		| 'match' if local and remote MD5s match, else time difference.
fileSize		| Number of bytes in file
sizeMatch		| 'match' if local and remote sizes match, else %local/remote.
revision                | Number of available revisions
ownerNames              | A list of owner user names
createdDate             | Created Time (UTC)
mimeType		| MIME file type
path                    | File path in Google Drive 
id                      | Unique [Google Drive File ID](https://developers.google.com/drive/api/v3/about-files)
shared                  | Is shared in Google Drive to other users (true/false)

## Google Drive Credentials

The configuration file also specifies the location of credentials for Google Drive and Ouath API access.

Name		| Description
:-----		| :-----
gdrive\_auth	| file path of Google Drive account authorization. Ignored if provided on command line.
oauth\_id	| file path of Google Oauth Client ID credentials. (App's permission to use API).

See the [Default YAML Configuration File](https://github.com/rich-murphey/kumodd/wiki/Default-configuration) for more details.

## HTTP Proxy

To optionally relay kumodd access though an HTTP proxy, specify the proxy in config/config.yml:
``` yaml
proxy:
  host: proxy.host.com
  port: 8888 (optional)
  user: username (optional)
  pass: password (optional)
```

