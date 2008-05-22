%define name idesk
%define version 0.7.5
%define release %mkrel 4

Version: 	%{version}
Summary: 	Plops icons on your root window
Name: 		%{name}
Release: 	%{release}
License: 	GPL
Group: 		Graphical desktop/Other
Source: 	%{name}-%{version}.tar.bz2
Patch0:		idesk-0.7.5-fix-fork.patch
Patch1:		idesk-0.7.5-invert-glowing.patch
Patch2:		idesk-0.7.5-restart-on-SIGHUP.patch
URL: 		http://idesk.sourceforge.net/
Buildrequires:	imlib2-devel gtk2-devel
Buildrequires:  libart_lgpl-devel startup-notification-devel
BuildRoot: 	%{_tmppath}/%{name}-buildroot


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

%build
%configure2_5x --enable-libsn
%make


%install
%__rm -rf %buildroot
%makeinstall

%clean
%__rm -rf %buildroot


%files
%defattr (-,root,root)
%doc README AUTHORS ChangeLog COPYING NEWS TODO
%{_bindir}/*
%{_datadir}/%{name}/

