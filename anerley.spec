%define major           0
%define libname         %mklibname %{name} %{major}
%define develname       %mklibname %{name} -d

Name: anerley
Summary: People widgets for Moblin
Group: System/Libraries
Version: 0.1.4
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: libglib2-devel
BuildRequires: libtelepathy-glib-devel
BuildRequires: libmissioncontrol-devel
BuildRequires: nbtk-devel
BuildRequires: gnome-common

%description
Anerley people widgets for Moblin

%package -n %{libname}
Summary: Anerley library for people widgets on Moblin
Group: Development/Libraries

%description -n %{libname}
Anerley people widgets for Moblin

%package -n %{develname}
Summary: Anerley development environment
Group: Development/C

Requires: %{libname} = %{version}-%{release}
Requires: pkgconfig
Requires: %{libname} >= %{version}

%description -n %{develname}
Header files and libraries for anerley

%prep
%setup -q -n %{name}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
	if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
		mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
	fi
done

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc COPYING NEWS AUTHORS README ChangeLog
%{_datadir}/%{name}/*
%{_libdir}/*.so.%{major}*
%{_datadir}/locale/*


%files -n %{develname}
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/anerley/*
%{_libdir}/pkgconfig/*.pc
