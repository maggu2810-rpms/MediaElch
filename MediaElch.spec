%global gittag v%{version}

Name:           MediaElch
Version:        2.10.4
Release:        2%{?dist}
Summary:        Media Manager for Kodi

License:        LGPL-3.0-only
URL:            https://mediaelch.github.io/mediaelch-doc/
Source0:        https://github.com/komet/mediaelch/archive/%{gittag}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  libmediainfo-devel
BuildRequires:  quazip-qt6-devel
Requires:       qt6-qtmultimedia
Requires:       qt6-qtsvg
Requires:       qt6-qt5compat
Requires:       quazip-qt6


%description
MediaElch is a MediaManager for Kodi.
Information about Movies, TV Shows, Concerts and Music are stored as NFO files.
Fanarts are downloaded automatically from fanart.tv.


%prep
%autosetup


%build
%cmake -DUSE_EXTERN_QUAZIP=ON -DMEDIAELCH_FORCE_QT6=ON
%cmake_build


%install
%cmake_install


%files
%{_bindir}/MediaElch
%{_datadir}/applications/MediaElch.desktop
%{_datadir}/metainfo/com.kvibes.MediaElch.metainfo.xml
%{_datadir}/pixmaps/MediaElch.png
%license COPYING
%doc CHANGELOG.md README.md


%changelog
* Fri Aug 11 2023 Markus Rathgeb <maggu2810@gmail.com>
- Initial package
