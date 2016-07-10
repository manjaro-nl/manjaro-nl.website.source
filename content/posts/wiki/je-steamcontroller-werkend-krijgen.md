Title: Je Steamcontroller werkend krijgen
Date: 2016-07-10 18:56
Category: wiki
Tags: steam
Slug: je-steamcontroller-werkend-krijgen
Status: published

Met de Steamsales achter de rug heb je misschien problemen gehad je Steamcontroller werkend te krijgen op Manjaro. Niet getreurd er is een eenvoudige fix.

<!-- PELICAN_END_SUMMARY -->

hernoem

`/usr/lib/udev/rules.d/80-steam-controller-permission.rules`

naar

`/usr/lib/udev/rules.d/70-steam-controller-permission.rules`



[bron](https://bugs.archlinux.org/task/47330#comment142957)
