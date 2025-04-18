#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v21
# autospec commit: be3faa5
#
Name     : p7zip
Version  : 17.06
Release  : 23
URL      : https://github.com/p7zip-project/p7zip/archive/v17.06/p7zip-17.06.tar.gz
Source0  : https://github.com/p7zip-project/p7zip/archive/v17.06/p7zip-17.06.tar.gz
Summary  : 7-zip file compression program
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-2.0 LGPL-2.1 LGPL-2.1+ MIT
Requires: p7zip-bin = %{version}-%{release}
Requires: p7zip-libexec = %{version}-%{release}
Requires: p7zip-license = %{version}-%{release}
BuildRequires : sed
BuildRequires : yasm
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: build.patch
Patch2: norar.patch

%description
p7zip is a quick port of 7z.exe and 7za.exe (command line version of
7zip, see www.7-zip.org) for Unix. 7-Zip is a file archiver with
highest compression ratio. Since 4.10, p7zip (like 7-zip) supports
little-endian and big-endian machines.

%package bin
Summary: bin components for the p7zip package.
Group: Binaries
Requires: p7zip-libexec = %{version}-%{release}
Requires: p7zip-license = %{version}-%{release}

%description bin
bin components for the p7zip package.


%package doc
Summary: doc components for the p7zip package.
Group: Documentation

%description doc
doc components for the p7zip package.


%package libexec
Summary: libexec components for the p7zip package.
Group: Default
Requires: p7zip-license = %{version}-%{release}

%description libexec
libexec components for the p7zip package.


%package license
Summary: license components for the p7zip package.
Group: Default

%description license
license components for the p7zip package.


%prep
%setup -q -n p7zip-17.06
cd %{_builddir}/p7zip-17.06
%patch -P 1 -p1
%patch -P 2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1741713416
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CFLAGS_GENERATE="$CLEAR_INTERMEDIATE_CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$CLEAR_INTERMEDIATE_FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$CLEAR_INTERMEDIATE_FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CLEAR_INTERMEDIATE_CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$CLEAR_INTERMEDIATE_LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CLEAR_INTERMEDIATE_CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$CLEAR_INTERMEDIATE_FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$CLEAR_INTERMEDIATE_FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CLEAR_INTERMEDIATE_CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$CLEAR_INTERMEDIATE_LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}"
make  %{?_smp_mflags}  all2 OPTFLAGS="$CFLAGS"

make %{?_smp_mflags} test
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}"
export GOAMD64=v2
make  %{?_smp_mflags}  all2 OPTFLAGS="$CFLAGS"


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CFLAGS_GENERATE="$CLEAR_INTERMEDIATE_CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$CLEAR_INTERMEDIATE_FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$CLEAR_INTERMEDIATE_FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CLEAR_INTERMEDIATE_CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$CLEAR_INTERMEDIATE_LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CLEAR_INTERMEDIATE_CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$CLEAR_INTERMEDIATE_FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$CLEAR_INTERMEDIATE_FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CLEAR_INTERMEDIATE_CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$CLEAR_INTERMEDIATE_LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1741713416
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/p7zip
cp %{_builddir}/p7zip-%{version}/C/brotli/LICENSE %{buildroot}/usr/share/package-licenses/p7zip/4763ba7dfa7730d98b190dd8a4a2c6818d301fcb || :
cp %{_builddir}/p7zip-%{version}/C/fast-lzma2/COPYING %{buildroot}/usr/share/package-licenses/p7zip/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8 || :
cp %{_builddir}/p7zip-%{version}/C/fast-lzma2/LICENSE %{buildroot}/usr/share/package-licenses/p7zip/6a6df164643ceac0f4870318e3ee69380532bbca || :
cp %{_builddir}/p7zip-%{version}/C/lizard/LICENSE %{buildroot}/usr/share/package-licenses/p7zip/6b87aff4027e85c03bba8bc9550a3b9f312901d0 || :
cp %{_builddir}/p7zip-%{version}/C/lz4/LICENSE %{buildroot}/usr/share/package-licenses/p7zip/10bf56381baaf07f0647b93a810eb4e7e9545e8d || :
cp %{_builddir}/p7zip-%{version}/C/lz5/LICENSE %{buildroot}/usr/share/package-licenses/p7zip/ed511439a52159987248d8e5090352d40cb92635 || :
cp %{_builddir}/p7zip-%{version}/C/zstd/COPYING %{buildroot}/usr/share/package-licenses/p7zip/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8 || :
cp %{_builddir}/p7zip-%{version}/C/zstd/LICENSE %{buildroot}/usr/share/package-licenses/p7zip/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c || :
cp %{_builddir}/p7zip-%{version}/C/zstdmt/LICENSE %{buildroot}/usr/share/package-licenses/p7zip/e1f8cfc4ba4bf9a77915701ac064a1c9531fb296 || :
cp %{_builddir}/p7zip-%{version}/CPP/7zip/Compress/Lzham/LICENSE %{buildroot}/usr/share/package-licenses/p7zip/d230bdc39b30bbbd1f0c86e6b80f6b298bdae88b || :
cp %{_builddir}/p7zip-%{version}/DOC/License.txt %{buildroot}/usr/share/package-licenses/p7zip/bab5d073942213e6db7faf375475a0740664acb0 || :
cp %{_builddir}/p7zip-%{version}/DOC/copying.txt %{buildroot}/usr/share/package-licenses/p7zip/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
GOAMD64=v2
%make_install
## install_append content
rm -rf %{buildroot}/usr/man/man1
rm -rf %{buildroot}/builddir/
sed -i  "s|%{buildroot}||g" %{buildroot}/usr/bin/*
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/7z
/usr/bin/7za

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/p7zip/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/p7zip/7z
/usr/libexec/p7zip/7z.so
/usr/libexec/p7zip/7zCon.sfx
/usr/libexec/p7zip/7za

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/p7zip/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/p7zip/10bf56381baaf07f0647b93a810eb4e7e9545e8d
/usr/share/package-licenses/p7zip/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/p7zip/4763ba7dfa7730d98b190dd8a4a2c6818d301fcb
/usr/share/package-licenses/p7zip/6a6df164643ceac0f4870318e3ee69380532bbca
/usr/share/package-licenses/p7zip/6b87aff4027e85c03bba8bc9550a3b9f312901d0
/usr/share/package-licenses/p7zip/bab5d073942213e6db7faf375475a0740664acb0
/usr/share/package-licenses/p7zip/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
/usr/share/package-licenses/p7zip/d230bdc39b30bbbd1f0c86e6b80f6b298bdae88b
/usr/share/package-licenses/p7zip/e1f8cfc4ba4bf9a77915701ac064a1c9531fb296
/usr/share/package-licenses/p7zip/ed511439a52159987248d8e5090352d40cb92635
