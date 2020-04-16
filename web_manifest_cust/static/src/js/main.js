odoo.define('web.ServiceWorkerMain', function (require) {
"use strict";

//add service worker js
(function checkServiceWorker() {
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/web_manifest_cust/static/src/js/service_worker.js').then(function(registration) {
            console.log('ServiceWorker registration successful with scope:',  registration.scope);
        }).catch(function(error) {
            console.log('ServiceWorker registration failed:', error);
        });
    });
  }
})();

});