#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3A6A4DB839EAA6D7 (aacid@kde.org)
#
Name     : lskat
Version  : 22.12.1
Release  : 49
URL      : https://download.kde.org/stable/release-service/22.12.1/src/lskat-22.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.1/src/lskat-22.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.1/src/lskat-22.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 LGPL-2.0
Requires: lskat-bin = %{version}-%{release}
Requires: lskat-data = %{version}-%{release}
Requires: lskat-license = %{version}-%{release}
Requires: lskat-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
GENERAL NOTE:
https://apps.kde.org/lskat

%package bin
Summary: bin components for the lskat package.
Group: Binaries
Requires: lskat-data = %{version}-%{release}
Requires: lskat-license = %{version}-%{release}

%description bin
bin components for the lskat package.


%package data
Summary: data components for the lskat package.
Group: Data

%description data
data components for the lskat package.


%package doc
Summary: doc components for the lskat package.
Group: Documentation

%description doc
doc components for the lskat package.


%package license
Summary: license components for the lskat package.
Group: Default

%description license
license components for the lskat package.


%package locales
Summary: locales components for the lskat package.
Group: Default

%description locales
locales components for the lskat package.


%prep
%setup -q -n lskat-22.12.1
cd %{_builddir}/lskat-22.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673280679
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1673280679
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lskat
cp %{_builddir}/lskat-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/lskat/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/lskat-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/lskat/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/lskat-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/lskat/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/lskat-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/lskat/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/lskat-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/lskat/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/lskat-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/lskat/a4c60b3fefda228cd7439d3565df043192fef137 || :
pushd clr-build
%make_install
popd
%find_lang lskat

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lskat

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.lskat.desktop
/usr/share/icons/hicolor/128x128/apps/lskat.png
/usr/share/icons/hicolor/16x16/apps/lskat.png
/usr/share/icons/hicolor/22x22/apps/lskat.png
/usr/share/icons/hicolor/32x32/apps/lskat.png
/usr/share/icons/hicolor/48x48/apps/lskat.png
/usr/share/icons/hicolor/64x64/apps/lskat.png
/usr/share/lskat/grafix/blue.desktop
/usr/share/lskat/grafix/blue.rc
/usr/share/lskat/grafix/blue.svg
/usr/share/lskat/grafix/egyptian.desktop
/usr/share/lskat/grafix/egyptian.rc
/usr/share/lskat/grafix/egyptian.svg
/usr/share/lskat/grafix/oxygen.desktop
/usr/share/lskat/grafix/oxygen.rc
/usr/share/lskat/grafix/oxygen.svg
/usr/share/metainfo/org.kde.lskat.appdata.xml
/usr/share/qlogging-categories5/lskat.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/lskat/index.cache.bz2
/usr/share/doc/HTML/ca/lskat/index.docbook
/usr/share/doc/HTML/cs/lskat/index.cache.bz2
/usr/share/doc/HTML/cs/lskat/index.docbook
/usr/share/doc/HTML/de/lskat/index.cache.bz2
/usr/share/doc/HTML/de/lskat/index.docbook
/usr/share/doc/HTML/en/lskat/index.cache.bz2
/usr/share/doc/HTML/en/lskat/index.docbook
/usr/share/doc/HTML/en/lskat/lskat_screen_01.png
/usr/share/doc/HTML/es/lskat/index.cache.bz2
/usr/share/doc/HTML/es/lskat/index.docbook
/usr/share/doc/HTML/et/lskat/index.cache.bz2
/usr/share/doc/HTML/et/lskat/index.docbook
/usr/share/doc/HTML/fr/lskat/index.cache.bz2
/usr/share/doc/HTML/fr/lskat/index.docbook
/usr/share/doc/HTML/fr/lskat/lskat_screen_01.png
/usr/share/doc/HTML/it/lskat/index.cache.bz2
/usr/share/doc/HTML/it/lskat/index.docbook
/usr/share/doc/HTML/nl/lskat/index.cache.bz2
/usr/share/doc/HTML/nl/lskat/index.docbook
/usr/share/doc/HTML/pt/lskat/index.cache.bz2
/usr/share/doc/HTML/pt/lskat/index.docbook
/usr/share/doc/HTML/pt_BR/lskat/index.cache.bz2
/usr/share/doc/HTML/pt_BR/lskat/index.docbook
/usr/share/doc/HTML/ru/lskat/index.cache.bz2
/usr/share/doc/HTML/ru/lskat/index.docbook
/usr/share/doc/HTML/sv/lskat/index.cache.bz2
/usr/share/doc/HTML/sv/lskat/index.docbook
/usr/share/doc/HTML/uk/lskat/index.cache.bz2
/usr/share/doc/HTML/uk/lskat/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lskat/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/lskat/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/lskat/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/lskat/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/lskat/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f lskat.lang
%defattr(-,root,root,-)

