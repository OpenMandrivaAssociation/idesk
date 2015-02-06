%define name idesk
%define version 0.7.5
%define release 7

Version: 	%{version}
Summary: 	Plops icons on your root window
Name: 		%{name}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Other
Source0: 	%{name}-%{version}.tar.bz2
Patch0:		idesk-0.7.5-fix-fork.patch
Patch1:		idesk-0.7.5-invert-glowing.patch
Patch2:		idesk-0.7.5-restart-on-SIGHUP.patch
patch3:		idesk-0.7.5.cstdlib.patch
URL: 		http://idesk.sourceforge.net/
Buildrequires:	imlib2-devel pkgconfig(gtk+-2.0)
Buildrequires:  libart_lgpl-devel startup-notification-devel
Buildrequires:	pkgconfig(xft)

%description
iDesk gives users of minimal wm's (fluxbox, pekwm, windowmaker...) icons on
their desktop. The icon graphics are either from a png or svg (vector) file
and support some eyecandy effects like transparency. Each icon can be
configured to run one or more shell commands and the actions which run
those commands are completely configurable.
In a nutshell if you want icons on your desktop and you don't have or don't
want KDE or gnome doing it, you can use idesk.

%prep

%setup -q
%{__perl} -pi.orig -e 's|/usr/local/share|%_datadir|g;' examples/default.lnk
%patch0 -p1 -b .fork
%patch1 -p1 -b .glow
%patch2 -p1 -b .HUP
%patch3 -p1 -b .cstdlib

%build
%configure2_5x --enable-libsn
%make

%install
%makeinstall

%files
%doc README AUTHORS ChangeLog COPYING NEWS TODO
%{_bindir}/*
%{_datadir}/%{name}/
