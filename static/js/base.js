document.getElementById('navLinkSearch').addEventListener("click", searchBar => {
    if (document.getElementById('searchInput').style.opacity === '1') {
        document.getElementById('searchInput').style.opacity = '0';
        document.getElementById('searchInput').style.height = '0em';
        document.getElementById('searchInput').style.pointerEvents = 'none';
        document.getElementById('dark').style.opacity = '0';
    }
    else {
        document.getElementById('searchInput').style.opacity = '1';
        document.getElementById('searchInput').style.height = '8em';
        document.getElementById('searchInput').style.pointerEvents = 'all';
        document.getElementById('dark').style.opacity = '1';
    }
})

document.getElementById('addToCartBtn').addEventListener('click', addToCart => {
    document.getElementById('addToCartBtn').innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="20" height="20" viewBox="0 0 172 172" style=" fill:#000000; margin-right: .5em;"><g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z" fill="none"></path><g fill="#ffffff"><path d="M86,17.2c-37.9948,0 -68.8,30.8052 -68.8,68.8c0,37.9948 30.8052,68.8 68.8,68.8c37.9948,0 68.8,-30.8052 68.8,-68.8c0,-12.49509 -3.38268,-24.17668 -9.20469,-34.27682l-64.4888,64.4776c-1.07213,1.07213 -2.52858,1.67969 -4.05364,1.67969c-1.51933,0 -2.98151,-0.60182 -4.05364,-1.67969l-25.53125,-25.53125c-2.24173,-2.24173 -2.24173,-5.86556 0,-8.10729c2.24173,-2.24173 5.86556,-2.24173 8.10729,0l21.4776,21.4776l61.92448,-61.92448c-12.61907,-15.222 -31.66081,-24.91536 -52.97734,-24.91536zM138.97734,42.11536c2.47479,2.98465 4.66412,6.21693 6.61797,9.59661l13.25833,-13.25833c2.24173,-2.24747 2.24173,-5.86556 0,-8.10729c-2.24173,-2.24173 -5.86556,-2.24173 -8.10729,0z"></path></g></g></svg> Added to cart';
})