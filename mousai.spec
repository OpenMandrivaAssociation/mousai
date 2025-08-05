%global	_enable_debug_packages  %{nil}

%define	oname	Mousai
%define	gitdate	20250727

Summary:	Identify any songs in seconds
Name:	mousai
Version:	0.7.8
Release:	2
License:	GPLv3+
Group:	Sound/Utilities
Url:	https://github.com/SeaDve/Mousai/
# Use a devel snapshot to pick up a year of fixes and updates
#Source0:	https://github.com/SeaDve/Mousai/releases/download/v%%{version}/%%{name}-%%{version}.tar.xz
Source0:	%{name}-%{gitdate}.tar.xz
Patch0:	mousai-0.7.8-add-DBus-service.patch
BuildRequires: appstream-util
BuildRequires: desktop-file-utils
BuildRequires: cargo
BuildRequires: gettext
BuildRequires: meson
BuildRequires: ninja
BuildRequires: rust
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-play-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(python)
Requires: typelib(Adw)
Requires: gtk4
Requires: python
Requires: python-gobject3
Requires: python3dist(pygobject)
Requires: python3dist(requests)

%description
Mousai is a simple application that can identify songs similar to Shazam.
Just click the listen button, and then wait a few seconds.  It will magically
return the title and artist of that song!
Note: This uses the API of audd.io, so it is necessary to log in to their site
to get more trials.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/metainfo/io.github.seadve.%{oname}.metainfo.xml
%{_datadir}/%{name}/resources.gresource
%{_datadir}/applications/io.github.seadve.%{oname}.desktop
%{_datadir}/glib-2.0/schemas/io.github.seadve.%{oname}.gschema.xml
%{_iconsdir}/hicolor/scalable/apps/io.github.seadve.%{oname}.svg
%{_iconsdir}/hicolor/symbolic/apps/io.github.seadve.%{oname}-symbolic.svg
%{_datadir}/dbus-1/services/io.github.seadve.%{oname}.service

#-----------------------------------------------------------------------------

%prep
#autosetup -n %%{name}-%%{version} -p1
%autosetup -n %{name}-%{gitdate} -p1


%build
%meson
%meson_build


%install
%meson_install

# Drop unknown locales
rm -rf %{buildroot}%{_datadir}/locale/zh_Hans/*
rm -rf %{buildroot}%{_datadir}/locale/zh_Hant/*

%find_lang %{name}
