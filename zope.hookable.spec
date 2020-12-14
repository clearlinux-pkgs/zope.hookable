#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.hookable
Version  : 5.0.1
Release  : 29
URL      : https://files.pythonhosted.org/packages/31/ce/4d1cd6d2a3d980989ceaf86abb6c8683f90f01a81861f3de6ec7ae317db7/zope.hookable-5.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/31/ce/4d1cd6d2a3d980989ceaf86abb6c8683f90f01a81861f3de6ec7ae317db7/zope.hookable-5.0.1.tar.gz
Summary  : Zope hookable
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.hookable-license = %{version}-%{release}
Requires: zope.hookable-python = %{version}-%{release}
Requires: zope.hookable-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
zope.hookable
        ===============

%package license
Summary: license components for the zope.hookable package.
Group: Default

%description license
license components for the zope.hookable package.


%package python
Summary: python components for the zope.hookable package.
Group: Default
Requires: zope.hookable-python3 = %{version}-%{release}

%description python
python components for the zope.hookable package.


%package python3
Summary: python3 components for the zope.hookable package.
Group: Default
Requires: python3-core
Provides: pypi(zope.hookable)
Requires: pypi(setuptools)

%description python3
python3 components for the zope.hookable package.


%prep
%setup -q -n zope.hookable-5.0.1
cd %{_builddir}/zope.hookable-5.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587405403
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.hookable
cp %{_builddir}/zope.hookable-5.0.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.hookable/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.hookable/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
