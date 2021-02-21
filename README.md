ert-downloader
==============

Αυτό το εργαλείο μπορεί να χρησιμοποιηθεί για να κατεβάσει βίντεο απο τον διαδυκτιακό χώρο της EΡΤ και του ertflix.

Υποστηρίζει τους ιστότοπους:
 - www.ertflix.gr
 - webtv.ert.gr
 - archive.ert.gr

αλλα θα προσπαθήσει να κατεβάσει και απο οποιονδήποτε άλλο του προσφέρετε.

Χρήση
=====

python ert-downloader.py [url]

για να κατεβάσετε ολόκληρα seasons, χρησιμοποιήστε για [url] το feed της σελίδας με τα επισόδεια,
π.χ. https://www.ertflix.gr/category/paidika/zig-sharko/feed
(στην πράξη, μπορείτε να δοκιμάσετε να προσθέσετε απλά το "/feed" σε οποιαδήποτε σελίδα με πολλαπλά thumbnails)

Παράδειγμα
=======

python ert-downloader.py https://webtv.ert.gr/xxxxxxxxxx/

Απαιτήσεις
============

Αυτο το εργαλείο απαιτεί την ύπαρξη του ffmpeg. Μπορείτε να το κατεβάσετε δωρεάν απο τον επίησμο του ιστότοπο: https://ffmpeg.org/download.html
Στη συνέχεια τοποθετήστε το αρχειο ffmpeg.exe στον ίδιο φάκελο με το εργαλείο.

Επισήμανση!
==========

Αυτό το εργαλείο δε πρέπει να χρησιμοποιηθεί για να γίνει λήψη περιεχομένου που τα πνευματκά δικαιώματα σας απαγορεύουν την ελεύθερη χρήση του.
Δεν προοθούμε τη χρήση του εργαλείου για πειρατικούς σκοπούς.

_______________________________________
ert-downloader
==============

This tool is used to download videos from Greece's public national channel webtv, EΡΤ, and ertflix.
It supports the domains:
 - www.ertflix.gr
 - webtv.ert.gr
 - archive.ert.gr

and will attempt to download any other link provided too.

Usage
=====

python ert-downloader.py [url]

To download whole series or collections, use the feed for the page with said series/collection as the [url]
i.e. https://www.ertflix.gr/category/paidika/zig-sharko/feed
(actually, you can try adding "/feed" to the url of any page with multiple thumbnails)

Example
=======

python ert-downloader.py https://webtv.ert.gr/xxxxxxxxxx/

Dependencies
============

This script relies on ffmpeg to encode the video. You can get it for free from the official source at https://ffmpeg.org/download.html
Put the file ffmpeg.exe at the root folder of the program.

Attention
==========

This program should not be used under any circumstances to download copyrighted material. We do not condone any sort of piracy using this tool.
