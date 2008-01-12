#
# Conditional build:
%bcond_without	aumix	# build without volume control
#
Summary:	An intelligent mp3 player
Summary(pl.UTF-8):	Inteligentny odtwarzacz mp3
Name:		cymbaline
Version:	1.3c
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://silmarill.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	698e795be504ce9d77e9a55021daa0c9
URL:		http://silmarill.org/cymbaline.htm
%{?with_aumix:BuildRequires:	aumix}
BuildRequires:	python-devel >= 1:2.0
BuildRequires:	python-mad
BuildRequires:	python-pyao-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cymbaline is a learning music player. It sets a score for each track
based on your listening habits, and you can set thresholds to create
playlists with your favorite tracks automatically. In random mode, it
will play your favorite tracks more often. It also allows album-based
navigation: you can start playing the next album, skip 2 albums ahead,
go to a specific album, etc.

%description -l pl.UTF-8
Cymbaline jest uczącym się odtwarzaczem muzyki. Ustawia on punkty dla
każdego utworu słuchanego przez użytkownika, który może ustawić
progi aby program mógł automatycznie stworzyć listy odtwarzania z
ulubionych utworów. W trybie losowym program będzie częściej
odtwarzał ulubione utwory użytkownika. Umożliwia on również
nawigację opartą na albumach: przejście to następnego albumu,
przejście o 2 albumy dalej, przejście do wybranego albumu itp.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install %{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitescriptdir}/*
