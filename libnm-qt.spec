%define major 5
%define libname %mklibname KF5NetworkManagerQt %{major}
%define devname %mklibname -d KF5NetworkManagerQt
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Qt5-only wrapper for NetworkManager DBus API
Name:		libnm-qt5
Version:	5.1.2
Release:	1
Epoch:		1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/libs/libnm-qt
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{plasmaver}/libnm-qt-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(ModemManager)
BuildRequires:	cmake(KF5ModemManagerQt)
BuildRequires:	pkgconfig(NetworkManager) >= 0.9.8.4
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	ninja

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
%{_libdir}/qt5/mkspecs/modules/*.pri

#----------------------------------------------------------------------------

%prep
%setup -qn libnm-qt-%{plasmaver}

%build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
ninja

%install
DESTDIR="%{buildroot}" ninja -C build install

