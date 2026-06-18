let click = 0;
function a() {
click++;
document.getElementById('click_html').innerHTML = click ;
}
function b() {
click--;
document.getElementById('click_html').innerHTML = click ;
}
function c() {
click=0;
document.getElementById('click_html').innerHTML = click ;
}
