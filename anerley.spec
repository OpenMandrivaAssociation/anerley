%define major           0
%define libname         %mklibname %{name} %{major}
%define develname       %mklibname %{name} -d

Name: anerley
Summary: People widgets for MeeGo
Group: System/Libraries
Version: 0.2.14
License: LGPL 2.1
URL: https://www.meego.com
Release: %mkrel 1
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: glib2-devel
BuildRequires: libtelepathy-glib-devel
BuildRequires: telepathy-mission-control-devel
BuildRequires: nbtk-devel
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: evolution-data-server-devel

%description
Anerley people widgets for MeeGo

%package -n %{libname}
Summary: Anerley library for people widgets on Moblin
Group: System/Libraries

%description -n %{libname}
Anerley people widgets for Moblin

%package -n %{develname}
Summary: Anerley development environment
Group: Development/C

Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel

%description -n %{develname}
Header files and libraries for anerley

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf --install
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

rm %{buildroot}%{_sysconfdir}/xdg/autostart/anerley-account-starter.desktop
rm %{buildroot}%{_libdir}/anerley-account-starter


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
