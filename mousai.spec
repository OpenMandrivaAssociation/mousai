%define _empty_manifest_terminate_build 0

%define oname   Mousai

Name:           mousai
Version:        0.7.7
Release:        1
Summary:        Identify any songs in seconds
License:        GPLv3.0
Group:          Sound/Utilities
Url:            https://github.com/SeaDve/Mousai/
#Source0:        https://github.com/SeaDve/Mousai/archive/refs/tags/v%{version}/%{oname}-%{version}.tar.gz
Source0:        https://github.com/SeaDve/Mousai/releases/download/v%{version}/mousai-%{version}.tar.xz

BuildRequires: meson
BuildRequires: cargo
BuildRequires: rust
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-play-1.0)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
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
%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/mousai
%{_datadir}/metainfo/io.github.seadve.Mousai.metainfo.xml
%{_datadir}/mousai/resources.gresource
%{_datadir}/applications/io.github.seadve.Mousai.desktop
%{_datadir}/glib-2.0/schemas/io.github.seadve.Mousai.gschema.xml
%{_iconsdir}/hicolor/scalable/apps/io.github.seadve.Mousai.svg
%{_iconsdir}/hicolor/symbolic/apps/io.github.seadve.Mousai-symbolic.svg
