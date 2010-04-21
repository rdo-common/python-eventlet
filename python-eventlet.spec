# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           python-eventlet
Version:        0.9.7
Release:        1%{?dist}
Summary:        Highly concurrent networking library
Group:          Development/Libraries
License:        MIT
URL:            http://eventlet.net
Source0:        http://pypi.python.org/packages/source/e/eventlet/eventlet-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%if 0%{?fedora} > 8
BuildRequires:  python-sphinx
BuildRequires:  python-greenlet
%endif
Requires:       python-greenlet

%description
Eventlet is a networking library written in Python. It achieves high
scalability by using non-blocking io while at the same time retaining
high programmer usability by using coroutines to make the non-blocking
io operations appear blocking at the source code level.

%if 0%{?fedora} > 11
%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for the python-eventlet package.
%endif


%prep
%setup -q -n eventlet-%{version}
find -name '.*' -type f -exec rm {} \;

%build
%{__python} setup.py build
%if 0%{?fedora} > 11
pushd doc
make html
rm _build/html/.buildinfo
popd
%endif

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{python_sitelib}/benchmarks
 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE NEWS README README.twisted
%{python_sitelib}/eventlet
%{python_sitelib}/eventlet*.egg-info

%if 0%{?fedora} > 11
%files doc
%defattr(-,root,root,-)
%doc doc/_build/html examples benchmarks tests
%endif

%changelog
* Wed Apr 14 2010 Lev Shamardin <shamardin@gmail.com> - 0.9.7-1
- Initial package version.
