# gnome-search-applet

This is a shell for a basic search applet. It's written in PyGTK.

The idea was to provide a way to search for applications directly from a Gnome panel. This doesn't *quite* implement that, but it's a start.

## Usage

1. Place the `SearchApplet.xml` file in `/usr/lib/bonobo/servers/` as `SearchApplet.server`. (You'll need root to do this.)
2. Restart the X server for it to show up.
3. Then add it using the 'Add Panel' option. It's called "Search Applet".

## Author

Copyright Nick Charlton 2012. Licensed under the GPL (because PyGTK, GTK and Gnome.)
