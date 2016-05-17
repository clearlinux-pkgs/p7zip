#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : p7zip
Version  : 15.14.1_src_all
Release  : 6
URL      : http://downloads.sourceforge.net/project/p7zip/p7zip/15.14.1/p7zip_15.14.1_src_all.tar.bz2
Source0  : http://downloads.sourceforge.net/project/p7zip/p7zip/15.14.1/p7zip_15.14.1_src_all.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: p7zip-bin
Requires: p7zip-lib
Requires: p7zip-doc
BuildRequires : cmake
BuildRequires : sed
Patch1: build.patch
Patch2: norar.patch

%description
p7zip 15.14.1
=============
Homepage : http://p7zip.sourceforge.net/
p7zip is a port of the Windows programs 7z.exe and 7za.exe provided by 7-zip.

%package bin
Summary: bin components for the p7zip package.
Group: Binaries

%description bin
bin components for the p7zip package.


%package doc
Summary: doc components for the p7zip package.
Group: Documentation

%description doc
doc components for the p7zip package.


%package lib
Summary: lib components for the p7zip package.
Group: Libraries

%description lib
lib components for the p7zip package.


%prep
%setup -q -n p7zip_15.14.1
%patch1 -p1
%patch2 -p1

%build
make V=1  %{?_smp_mflags} all2

%install
rm -rf %{buildroot}
%make_install
## make_install_append content
rm -rf %{buildroot}/usr/man/man1
rm -rf %{buildroot}/builddir/
sed -i  "s|%{buildroot}||g" %{buildroot}/usr/bin/*
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib/p7zip/7z
/usr/lib/p7zip/7zCon.sfx
/usr/lib/p7zip/7za

%files bin
%defattr(-,root,root,-)
/usr/bin/7z
/usr/bin/7za

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/p7zip/*

%files lib
%defattr(-,root,root,-)
/usr/lib/p7zip/7z.so
