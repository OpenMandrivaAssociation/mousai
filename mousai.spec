%define oname   Mousai

Name:           mousai
Version:        0.6.6
Release:        1
Summary:        Identify any songs in seconds
License:        GPLv3.0
Group:          Sound/Utilities
Url:            https://github.com/SeaDve/Mousai/
Source0:        https://github.com/SeaDve/Mousai/archive/refs/tags/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires: meson

%description
Mousai is a simple application that can identify songs similar to Shazam. Just click the listen button, and then wait a few seconds. 
It will magically return the title and artist of that song!
Note: This uses the API of audd.io, so it is necessary to log in to their site to get more trials.
