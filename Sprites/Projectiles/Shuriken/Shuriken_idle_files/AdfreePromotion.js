    var setCookie = function (cname, cvalue, exhour, path, domain) {
        var d = new Date();
        d.setTime(d.getTime() + (exhour * 60 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path=" + path + ";domain=" + domain;
    };
    var getCookie = function (cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    };
    var generatePromotionModal = function (modalId, callback) {
        var AdfreePromotionModalHtml = '<!-- Promotional Modal -->';
        AdfreePromotionModalHtml += '<div class="modal fade bs-example-modal-sm" id="' + modalId + '" tabindex="-1" role="dialog" aria-labelledby="' + modalId + 'Label" style="top: -1000%; max-height:700px;width:850px;">';
        AdfreePromotionModalHtml += '<div class="modal-dialog" role="document">';
        AdfreePromotionModalHtml += '<div class="modal-content">';
        AdfreePromotionModalHtml += '<div class="modal-header">';
        AdfreePromotionModalHtml += '<button type="button" class="close" data-dismiss="modal" aria-label="Close" style="position: absolute; right: 9px; top: 5px;"><span aria-hidden="true">&times;</span></button>';
        AdfreePromotionModalHtml += '</div>';
        AdfreePromotionModalHtml += '<div class="modal-body" style="padding: 17px 20px 2px 20px">';

//        // MIXPANEL SCRIPT ADDED
//        AdfreePromotionModalHtml += '<!-- start Mixpanel --><script type="text/javascript">(function(e, a) { if (!a.__SV) { var b = window; try { var c, l, i, j = b.location, g = j.hash; c = function(a, b) { return (l = a.match(RegExp(b + "=([^&]*)"))) ? l[1] : null }; g && c(g, "state") && (i = JSON.parse(decodeURIComponent(c(g, "state"))), "mpeditor" === i.action && (b.sessionStorage.setItem("_mpcehash", g), history.replaceState(i.desiredHash || "", e.title, j.pathname + j.search))) } catch (m) {} var k, h; window.mixpanel = a; a._i = []; a.init = function(b, c, f) { function e(b, a) { var c = a.split("."); 2 == c.length && (b = b[c[0]], a = c[1]); b[a] = function() { b.push([a].concat(Array.prototype.slice.call(arguments, 0))) } } var d = a; "undefined" !== typeof f ? d = a[f] = [] : f = "mixpanel"; d.people = d.people || []; d.toString = function(b) { var a = "mixpanel"; "mixpanel" !== f && (a += "." + f); b || (a += " (stub)"); return a }; d.people.toString = function() { return d.toString(1) + ".people (stub)" }; k = "disable time_event track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config reset people.set people.set_once people.increment people.append people.union people.track_charge people.clear_charges people.delete_user".split(" "); for (h = 0; h< k.length; h++) e(d, k[h]); a._i.push([b, c, f]) }; a.__SV=1 .2; b=e .createElement( "script"); b.type="text/javascript" ; b.async=! 0; b.src="undefined" !==t ypeof MIXPANEL_CUSTOM_LIB_URL ? MIXPANEL_CUSTOM_LIB_URL : "file:"===e .location.protocol && "//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js".match(/^\\/\\//) ? "https://cdn.mxpnl.com/libs/mixpanel-2-latest.min.js" : "//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js"; c=e .getElementsByTagName( "script")[0]; c.parentNode.insertBefore(b, c) } })(document, window.mixpanel || []); mixpanel.init( "a5cb3dda6e2c7bf7f31fec9ff2174632"); </script><!-- end Mixpanel -->';


//        // MIXPANEL CALLING FOR MODAL AD
//        AdfreePromotionModalHtml += '<script type="text/javascript">';
//        AdfreePromotionModalHtml += 'mixpanel.track_links("#modalImage", "Clicked Print Skyscraper", {';
//        AdfreePromotionModalHtml += '"Domain": "photobucket.com"';
//        AdfreePromotionModalHtml += '});';
//        AdfreePromotionModalHtml += '</script>';


        AdfreePromotionModalHtml += '<div style="width:422px;margin: 0 auto;">';
//        AdfreePromotionModalHtml += '<div style="height: 125px; background-color:#e3f3ff; font-family: \'gblack\'; font-size: 35.8px; color: #3fa9f5; text-align:center; padding: 24px 0; box-sizing: border-box; line-height: 42px">';
//        AdfreePromotionModalHtml += 'ALL PHOTOS';
//        AdfreePromotionModalHtml += '<span style="display:block; font-family: \'gmedium\';">ZERO ADS</span>';
//        AdfreePromotionModalHtml += '</div>';
//        AdfreePromotionModalHtml += '<div style="background-color:#43a0e2; height:74px; font-family: \'gblack\'; font-size: 23.5px; color: #ffffff; text-align:center; padding: 15px 0; box-sizing: border-box;">';
//        AdfreePromotionModalHtml += 'Go AD Free for just $0.99/mo';
//        AdfreePromotionModalHtml += '<span style="display:block; font-family: \'gmedium\'; font-style: italic; font-size: 16px; padding-top:5px">(only $9.99 a year)</span>';
//        AdfreePromotionModalHtml += '</div>';
        AdfreePromotionModalHtml += '<div style="height:602px; overflow: hidden; position:relative">';
        AdfreePromotionModalHtml += "<a href='https://secure.photobucket.com/plus?tier=8' onclick=\"Pb.Component.Tracking.Mixpanel.track('Clicked Plus 20 Skyscraper', {'button location': 'go ad print'});\">";
        AdfreePromotionModalHtml += '<img src="http://i12.photobucket.com/albums/a206/zxc6/1_zps3e6rjofn.jpg" width="422" border="0" id="modalImage">';
        AdfreePromotionModalHtml += '</a>';
//        AdfreePromotionModalHtml += '<a href="/pricing" id="upgradeButton" class="btn-sign" data-tracking="PlusAdFree_logged_out" style="position: absolute; background-color: #3fa9f5; display: block; width:196px; height:39px; bottom:29px; left:114px; color:#ffffff; text-align:center; line-height:39px; text-decoration:none; font-family: \'gbold\'; font-size:16px;">';
//        AdfreePromotionModalHtml += 'UPGRADE';
//        AdfreePromotionModalHtml += '</a>';

        AdfreePromotionModalHtml += '</div>';
        AdfreePromotionModalHtml += '</div>';
        AdfreePromotionModalHtml += '</div>';
        AdfreePromotionModalHtml += '<div class="modal-footer">';
//        AdfreePromotionModalHtml += '<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>';
//        AdfreePromotionModalHtml += '<button type="button" class="btn btn-primary">Save changes</button>';
        AdfreePromotionModalHtml += '<div id="videoAdModal"><iframe style="width: 728px; height: 90px; margin-left: 30px;" class="bannerAdIframe" id="bannerAd" frameborder="0" scrolling="no" data-type="BANNER" data-width="728" marginwidth="0" marginheight="0" src="http://photobucket.adnxs.com/pt?inv_code=fs_PETSANDANIMALS_CATS&amp;size=728x90&amp;age=19&amp;gender=M&amp;member=86&amp;redir=//b.photobucket.com/pbkt/hserver/viewid=588429095/size=BANNER/random=604299/area=fs_PETSANDANIMALS_CATS/age=19/gender=M/reg_zip=1124235/username=zxc6/login=Y/utype=free/ba=/sp=f/ownername=empty/search_kw=cat/ptype=browse/pos=no_inf/likes=n/spon=empty/adCount=empty/bl=0/ref_domain=empty/feature=search_urlphx/site=pb2/track=empty/slid=0/ilab=0/glam728%3D/gadadid%3D/gadsz%3D728x90/gadreqid%3D/anprice={PRICEBUCKET}/generic={BIDURLENC}"></iframe></div>';
        AdfreePromotionModalHtml += '</div>';
        AdfreePromotionModalHtml += '</div>';

        callback(AdfreePromotionModalHtml);
    };
    var resetInterval = function () {
//        setTimeout(function () {
        if (typeof isFreeUser != 'undefined') {
            if (isFreeUser) {
                if (!$("#" + modalId).hasClass('in')) {
                    $("#" + modalId).modal('show');
                }
            }
        }
        else {
            if (!$("#" + modalId).hasClass('in')) {
                $("#" + modalId).modal('show');
            }
        }
//        }, showModalInterval);
    };
    var allCookieArray = function () {
        var cookieArray = [];
        $.each(document.cookie.split('; '), function (key, item) {
            var eachItem = item.split('=');
            if (eachItem.length > 1) {
                cookieArray[eachItem[0]] = eachItem[1];
            }
        });
        return cookieArray;
    };
    var removeAdFrame = function () {
        $("#myModal").remove();
        if ($("#content .ad.skyscraperAd.promotion").length > 0) {
            $("#content .ad.skyscraperAd.promotion").remove();
        }
        else if ($("#main .content .ad.skyscraperAd.promotion").length > 0) {
            $("#main .content .ad.skyscraperAd.promotion").remove();
        }
//        if ($("#myModal .modal-body .ad.skyscraperAd.promotion").length > 0) {
//            $("#myModal .modal-body .ad.skyscraperAd.promotion").remove();
//            $("#myModal").remove();
//        }
    };
    var allCookies = [];
    var whiteUrls = ['/loginbox', '/login', '/register', '/mobile', '/pricing', '/pricing/adfree', '/plus', '/plus/details', '/plus/payment', '/plus/confirmation'];

    var modalId = 'myModal';
    var showModalInterval = 10000;
    var isMobile = false;
    $(document).on('show.bs.modal', '#' + modalId, function (e) {
        // CALLED WHEN MODAL INITIATE
//        $(window).trigger('adfreePromotionalModalAdRefresh');
    });
    $(document).on('shown.bs.modal', '#' + modalId, function (e) {
        // CALLED WHEN MODAL SHOWED
        $('body').css({overflow: 'hidden'});
        setCookie('isModalOpened', true, 8, '/', '.photobucket.com');
    });
    $(document).on('hide.bs.modal', '#' + modalId, function (e) {
        // CALLED WHEN MODAL HIDE INITIATE
//        return e.preventDefault();
        $('body').css({overflow: 'visible'});
    });
    $(document).on('hidden.bs.modal', '#' + modalId, function (e) {
        // CALLED WEHN MODAL HIDED
        removeAdFrame();
    });
    $(document).on('loaded.bs.modal', '#' + modalId, function (e) {
        // CALLED WHEN THE MDAL LOADED CONTENT REMOTELY
    });

    $(function () {
//        $('head').append('<script type="text/javascript">var isFreeUser = false;<\/script>');

        // PLACING THE PROMOTION MODAL INTO BODY GLOBALLY
        generatePromotionModal(modalId, function (response) {
            $('body').append(response);

            var modalCSS = '<style type="text/css">';
            modalCSS += '@font-face {';
            modalCSS += "font-family: 'gbook';";
            modalCSS += "src: url('/resources/fonts/promotion-modal/GothamBook.eot');";
            modalCSS += "src: url('/resources/fonts/promotion-modal/GothamBook.eot') format('embedded-opentype'), url('/resources/fonts/promotion-modal/GothamBook.woff2') format('woff2'), url('/resources/fonts/promotion-modal/GothamBook.woff') format('woff'),url('/resources/fonts/promotion-modal/GothamBook.ttf') format('truetype'), url('/resources/fonts/promotion-modal/GothamBook.svg#GothamBook') format('svg');";
            modalCSS += "}";
            modalCSS += "@font-face {";
            modalCSS += "font-family: 'gblack';";
            modalCSS += "src: url('/resources/fonts/promotion-modal/GOTHAMBLACK.eot');";
            modalCSS += "src: url('/resources/fonts/promotion-modal/GOTHAMBLACK.eot') format('embedded-opentype'), url('/resources/fonts/promotion-modal/GOTHAMBLACK.woff2') format('woff2'), url('/resources/fonts/promotion-modal/GOTHAMBLACK.woff') format('woff'), url('/resources/fonts/promotion-modal/GOTHAMBLACK.ttf') format('truetype'), url('/resources/fonts/promotion-modal/GOTHAMBLACK.svg#GOTHAMBLACK') format('svg');";
            modalCSS += "}";
            modalCSS += "@font-face {";
            modalCSS += "font-family: 'gbold';";
            modalCSS += "src: url('/resources/fonts/promotion-modal/GOTHAMBOLD.eot');";
            modalCSS += "src: url('/resources/fonts/promotion-modal/GOTHAMBOLD.eot') format('embedded-opentype'), url('/resources/fonts/promotion-modal/GOTHAMBOLD.woff2') format('woff2'), url('/resources/fonts/promotion-modal/GOTHAMBOLD.woff') format('woff'), url('/resources/fonts/promotion-modal/GOTHAMBOLD.ttf') format('truetype'), url('/resources/fonts/promotion-modal/GOTHAMBOLD.svg#GOTHAMBOLD') format('svg');";
            modalCSS += "}";
            modalCSS += "@font-face {";
            modalCSS += "font-family: 'glight';";
            modalCSS += "src: url('/resources/fonts/promotion-modal/GOTHAMLIGHT.eot');";
            modalCSS += "src: url('/resources/fonts/promotion-modal/GOTHAMLIGHT.eot') format('embedded-opentype'), url('/resources/fonts/promotion-modal/GOTHAMLIGHT.woff2') format('woff2'), url('/resources/fonts/promotion-modal/GOTHAMLIGHT.woff') format('woff'), url('/resources/fonts/promotion-modal/GOTHAMLIGHT.ttf') format('truetype'), url('/resources/fonts/promotion-modal/GOTHAMLIGHT.svg#GOTHAMLIGHT') format('svg');";
            modalCSS += "}";
            modalCSS += "@font-face {";
            modalCSS += "font-family: 'gmedium';";
            modalCSS += "src: url('/resources/fonts/promotion-modal/GothamMedium.eot');";
            modalCSS += "src: url('/resources/fonts/promotion-modal/GothamMedium.eot') format('embedded-opentype'), url('/resources/fonts/promotion-modal/GothamMedium.woff2') format('woff2'), url('/resources/fonts/promotion-modal/GothamMedium.woff') format('woff'), url('/resources/fonts/promotion-modal/GothamMedium.ttf') format('truetype'), url('/resources/fonts/promotion-modal/GothamMedium.svg#GothamMedium') format('svg');";
            modalCSS += "}";
            modalCSS += "@font-face {";
            modalCSS += "font-family: 'gthin';";
            modalCSS += "src: url('/resources/fonts/promotion-modal/gotham_thin.eot');";
            modalCSS += "src: url('/resources/fonts/promotion-modal/gotham_thin.eot') format('embedded-opentype'), url('/resources/fonts/promotion-modal/gotham_thin.woff2') format('woff2'), url('/resources/fonts/promotion-modal/gotham_thin.woff') format('woff'), url('/resources/fonts/promotion-modal/gotham_thin.ttf') format('truetype'), url('/resources/fonts/promotion-modal/gotham_thin.svg#gotham_thin') format('svg');";
            modalCSS += "}";
            modalCSS += '.ad.skyscraperAd.left.promotion{float: left;}.ad.skyscraperAd.right.promotion{float: right;}';
            modalCSS += '</style>';

            $("#myModal .modal-body").prepend(modalCSS);


            if ($("#main .content .ad.skyscraperAd.promotion").length > 0) {
                $("#myModal .modal-body").prepend($("#main .content .ad.skyscraperAd.promotion").removeClass('hide'));
            }
            else if ($("#content .ad.skyscraperAd.promotion").length > 0) {
                $("#myModal .modal-body").prepend($("#content .ad.skyscraperAd.promotion").removeClass('hide'));
            }

            $("#myModal .modal-body").prepend('<iframe style="width: 728px; height: 90px; margin-left: 30px;" class="bannerAdIframe" id="bannerAd" frameborder="0" scrolling="no" data-type="BANNER" data-width="728" marginwidth="0" marginheight="0" src="http://photobucket.adnxs.com/pt?inv_code=fs_PETSANDANIMALS_CATS&amp;size=728x90&amp;age=19&amp;gender=M&amp;member=86&amp;redir=//b.photobucket.com/pbkt/hserver/viewid=588429095/size=BANNER/random=604299/area=fs_PETSANDANIMALS_CATS/age=19/gender=M/reg_zip=1124235/username=zxc6/login=Y/utype=free/ba=/sp=f/ownername=empty/search_kw=cat/ptype=browse/pos=no_inf/likes=n/spon=empty/adCount=empty/bl=0/ref_domain=empty/feature=search_urlphx/site=pb2/track=empty/slid=0/ilab=0/glam728%3D/gadadid%3D/gadsz%3D728x90/gadreqid%3D/anprice={PRICEBUCKET}/generic={BIDURLENC}"></iframe>');

//            var callingVideo = setInterval(function () {
//                if ($("#videoAdModal").html() != "") {
//                    if (callingVideo) {
//                        clearInterval(callingVideo);
//                    }
//                }
//                else {
//                    Pb.Component.Ad.VideoAdModal.playAd(795, 360);
//                }
//            }, 2000);
            $(window).trigger('adfreePromotionalModalAdRefresh');
        });

    });
    $(window).load(function () {
        allCookies = allCookieArray();

        isMobile = ($.inArray('pb_mobile', allCookies) && allCookies['pb_mobile'] == 'true') ? true : false;
        if (!isMobile) {

            if ($.inArray(window.location.pathname, whiteUrls) == -1) {
                if (getCookie('isModalOpened') == "" || getCookie('isModalOpened') == 'false') {
                    resetInterval();
                }
                else {
                    removeAdFrame();
                }
            }
            else {
                removeAdFrame();
            }
        }
    });

    