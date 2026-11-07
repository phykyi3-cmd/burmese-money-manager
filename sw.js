const CACHE_NAME = 'burmese-money-manager-v36';
const STATIC_ASSETS = [
  './',
  './index.html',
  './Burmese-Money-Manager.html',
  './privacy.html',
  './terms.html',
  './delete-account.html',
  './BurmeseMoneyManager.mobileconfig',
  './tailwind.min.css',
  './lucide.min.js',
  './landing.html',
  './manifest.json',
  './icon.svg',
  './apple-touch-icon.png',
  './icon-192.png',
  './icon-512.png',
  './assets/3d_money_bag.jpg',
  './assets/gmail.png',
  './assets/banks/kpay.png',
  './assets/banks/wave.png',
  './assets/banks/ayapay.png',
  './assets/banks/cbbank.png',
  './assets/banks/yoma.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[SW v22] Pre-caching core assets for Burmese Money Manager (100% offline capability)');
      return cache.addAll(STATIC_ASSETS).catch(err => {
        console.warn('[SW] Pre-cache warning:', err);
      });
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[SW v22] Purging previous cache version:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Network-First for HTML navigation so phones update instantly; Cache-First for static assets
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  const url = new URL(event.request.url);
  const isNavigate = event.request.mode === 'navigate' || url.pathname.endsWith('.html') || url.pathname.endsWith('/');

  if (isNavigate) {
    // Network-First Strategy for HTML: ensures user immediately gets latest code when online
    event.respondWith(
      fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          }
          return networkResponse;
        })
        .catch(() => {
          // Fallback to cache when offline
          return caches.match(event.request).then((cached) => {
            return cached || caches.match('./index.html');
          });
        })
    );
  } else {
    // Stale-While-Revalidate Strategy for assets
    event.respondWith(
      caches.match(event.request).then((cachedResponse) => {
        const fetchPromise = fetch(event.request).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          }
          return networkResponse;
        }).catch(() => {});

        return cachedResponse || fetchPromise;
      })
    );
  }
});
