%define major 5
%define libname %mklibname KF5NetworkManagerQt %{major}
%define devname %mklibname -d KF5NetworkManagerQt
%define debug_package %{nil}

Summary:	Qt5-only wrapper for NetworkManager DBus API
Name:		libnm-qt5
Version:	5.0.91
Release:	1
Epoch:		1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/libs/libnm-qt
Source0:	ftp://ftp.kde.org/pub/kde/stable/plasma/5.0.0/src/libnm-qt-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(ModemManager)
BuildRequires:	cmake(KF5ModemManagerQt)
BuildRequires:	pkgconfig(NetworkManager) >= 0.9.8.4
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-util)

%description
Qt5 library for NetworkManager.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Qt5-only wrapper for NetworkManager DBus API
Group:		System/Libraries
Conflicts:	%{_lib}nm-qt0 < 1:0.9.8.1
Obsoletes:	%{_lib}nm-qt0 < 1:0.9.8.1

%description -n %{libname}
Qt5 library for NetworkManager.

%files -n %{libname}
%{_libdir}/libKF5NetworkManagerQt.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Conflicts:	%{_lib}nm-qt-devel < 1:0.9.8.1
Obsoletes:	%{_lib}nm-qt-devel < 1:0.9.8.1

%description -n %{devname}
Qt libraries and header files for developing applications
that use NetworkManager.

%files -n %{devname}
%{_libdir}/libKF5NetworkManagerQt.so
%{_includedir}/KF5/NetworkManagerQt/
%{_includedir}/KF5/networkmanagerqt_version.h
%{_libdir}/cmake/KF5NetworkManagerQt
%{_prefix}/mkspecs/modules/*.pri

#----------------------------------------------------------------------------

%prep
%setup -qn libnm-qt-%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build

