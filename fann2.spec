#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fann2
Version  : 1.1.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/80/a1/fed455d25c34a62d4625254880f052502a49461a5dd1b80854387ae2b25f/fann2-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/80/a1/fed455d25c34a62d4625254880f052502a49461a5dd1b80854387ae2b25f/fann2-1.1.2.tar.gz
Summary  : Fast Artificial Neural Network Library (FANN) Python bindings.
Group    : Development/Tools
License  : LGPL-2.1
Requires: fann2-license = %{version}-%{release}
Requires: fann2-python = %{version}-%{release}
Requires: fann2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : fann-dev
BuildRequires : swig

%description
README
        ======
        
        
        fann2
        =====
        
        Python bindings for Fast Artificial Neural Networks 2.2.0 (FANN >= 2.2.0). These
        are the original python bindings included with FANN 2.1.0 beta and updated to
        include support for python 2.6-3.6.
        
        
        DESCRIPTION
        ===========
        
        This is a python binding for Fast Artificial Neural Network Library (FANN >=
        2.2.0) that implements multi-layer artificial neural networks with support for
        both fully-connected and sparsely-connected networks. It includes a framework
        for easily handling training data sets. It is easy to use, versatile, well-
        documented, and fast.
        
        FANN 2.2.0 source
        -----------------

%package license
Summary: license components for the fann2 package.
Group: Default

%description license
license components for the fann2 package.


%package python
Summary: python components for the fann2 package.
Group: Default
Requires: fann2-python3 = %{version}-%{release}

%description python
python components for the fann2 package.


%package python3
Summary: python3 components for the fann2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the fann2 package.


%prep
%setup -q -n fann2-1.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541268534
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fann2
cp LICENSE %{buildroot}/usr/share/package-licenses/fann2/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fann2/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
