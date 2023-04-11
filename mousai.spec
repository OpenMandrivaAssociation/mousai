%define _empty_manifest_terminate_build 0

%define oname   Mousai

Name:           mousai
Version:        0.7.0
Release:        1
Summary:        Identify any songs in seconds
License:        GPLv3.0
Group:          Sound/Utilities
Url:            https://github.com/SeaDve/Mousai/
#Source0:        https://github.com/SeaDve/Mousai/archive/refs/tags/v%{version}/%{oname}-%{version}.tar.gz
Source0:        https://github.com/SeaDve/Mousai/releases/download/v%{version}/mousai-%{version}.tar.xz

BuildRequires: meson
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(python)
BuildRequires: appstream-util

Requires: typelib(Adw)
Requires: gtk4
Requires: python
Requires: python-gobject3
Requires: python3dist(pygobject)
Requires: python3dist(requests)

%description
Mousai is a simple application that can identify songs similar to Shazam. Just click the listen button, and then wait a few seconds. 
It will magically return the title and artist of that song!
Note: This uses the API of audd.io, so it is necessary to log in to their site to get more trials.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/mousai
%{_datadir}/appdata/io.github.seadve.Mousai.appdata.xml
%{_datadir}/applications/io.github.seadve.Mousai.desktop
%{_datadir}/glib-2.0/schemas/io.github.seadve.Mousai.gschema.xml
%{_datadir}/mousai/mousai*
%{_iconsdir}/hicolor/scalable/apps/io.github.seadve.Mousai.svg
%{_iconsdir}/hicolor/symbolic/apps/io.github.seadve.Mousai-symbolic.svg
