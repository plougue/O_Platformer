window.hjSiteSettings = window.hjSiteSettings || {"testers_widgets":[],"surveys":[],"record_targeting_rules":[],"recording_capture_keystrokes":true,"polls":[],"site_id":242358,"forms":[],"record":false,"heatmaps":[{"targeting":[{"negate":false,"pattern":"https:\/\/print.photobucket.com\/","match_operation":"exact","component":"url"}],"created_epoch_time":1468274017,"id":637497,"selector_version":0}],"deferred_page_contents":[{"targeting":[{"negate":false,"pattern":"https:\/\/print.photobucket.com\/","match_operation":"exact","component":"url"},{"negate":false,"pattern":"desktop","match_operation":"exact","component":"device"}],"id":1602043},{"targeting":[{"negate":false,"pattern":"https:\/\/print.photobucket.com\/","match_operation":"exact","component":"url"},{"negate":false,"pattern":"tablet","match_operation":"exact","component":"device"}],"id":1602042},{"targeting":[{"negate":false,"pattern":"https:\/\/print.photobucket.com\/","match_operation":"exact","component":"url"},{"negate":false,"pattern":"phone","match_operation":"exact","component":"device"}],"id":1602041}],"feedback_widgets":[],"r":0.0731675185,"state_change_listen_mode":"manual"};

window.hjBootstrap = window.hjBootstrap || function (scriptUrl) {
    var b = function () {}, d = document, h = d.head || d.getElementsByTagName('head')[0], s, v, c, ct;

    if (!d.addEventListener) {
        return;
    }

    s = d.createElement('script');
    s.async = 1;
    s.src = scriptUrl;
    h.appendChild(s);

    ct = [
        'iframe#_hjRemoteVarsFrame {',
        'display: none !important; width: 1px !important; height: 1px !important; ' +
        'opacity: 0 !important; pointer-events: none !important;',
        '}'
    ];
    c = document.createElement('style');
    c.type = 'text/css';
    if (c.styleSheet) {
        c.styleSheet.cssText = ct.join('');
    } else {
        c.appendChild(d.createTextNode(ct.join('')));
    }
    h.appendChild(c);

    v = d.createElement('iframe');
    v.style.cssText = ct[1];
    v.name = '_hjRemoteVarsFrame';
    v.title = 'Hotjar Remote Vars Frame';
    v.id = '_hjRemoteVarsFrame';
    v.src = 'https://' + (window._hjSettings.varsHost || 'vars.hotjar.com') + '/rcj-b2c1bce0a548059f409c021a46ea2224.html';
    v.onload = function () {
        b.varsLoaded = true;
        if ((typeof hj != 'undefined') && hj.event) {
            hj.event.signal('varsLoaded');
        }
    };
    b.varsJar = v;

    if (d.body) {
        d.body.appendChild(v);
    } else {
        d.addEventListener('DOMContentLoaded', function () {
            d.body.appendChild(v);
        });
    }
    window.hjBootstrap = b;
};


hjBootstrap('https://script.hotjar.com/modules-05ea6e00ffc1020d4cf8d62885964e4c.js');