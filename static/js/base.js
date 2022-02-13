




document.getElementById('navLinkSearch').addEventListener("click", searchBar => {
    if (document.getElementById('searchInput').style.opacity === '1') {
        document.getElementById('searchInput').style.opacity = '0';
        document.getElementById('searchInput').style.height = '0em';
        document.getElementById('dark').style.opacity = '0';
    }
    else {
        document.getElementById('searchInput').style.opacity = '1';
        document.getElementById('searchInput').style.height = '8em';
        document.getElementById('dark').style.opacity = '1';
    }
})