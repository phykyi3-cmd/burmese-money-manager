# 🛡️ BURMESE MONEY MANAGER - DATA PRESERVATION & SAFETY CONTRACT

> **IMMUTABLE GOLDEN RULE**:
> Any application update, feature release, Service Worker upgrade, or UI redesign must **NEVER** clear, alter, or lose existing user data.
> All updates must be **100% non-destructive and backward-compatible**.

---

## 1. Storage Separation Architecture
* **Code & Asset Layer (Ephemeral / Replaceable)**:
  * Handled exclusively by the **Service Worker Cache API** (`burmese-money-manager-vXX`).
  * Stores: `index.html`, `tailwind.min.css`, `lucide.min.js`, icons, fonts, and images.
  * When a new version is published, the Cache API purges *only* old HTML/JS/CSS assets and fetches new code.
* **User Data Layer (Permanent & Protected)**:
  * Handled exclusively by **localStorage** and **Encrypted Cloud Store**.
  * Stores:
    * `mm_user_registry`: User authentication registry & profiles.
    * `mm_active_session_id`: Currently logged-in user ID.
    * `mm_u_${userId}_accounts`: Bank & wallet balances.
    * `mm_u_${userId}_transactions`: Complete financial ledger & expense logs.
    * `mm_u_${userId}_goals`: User-created savings goals & target wishlist.
    * `mm_u_${userId}_budget`: User's monthly budget limit.
    * `mm_lang`, `mm_currency`, `mm_wallpaper`: User appearance & locale preferences.
  * **Service Worker upgrades have ZERO access to, and CANNOT touch, localStorage.**

---

## 2. Non-Destructive Update Rules for Developers & Agents
1. **Never call `localStorage.clear()`**:
   * Global `localStorage.clear()` is strictly forbidden in production code.
2. **Additive Schema Migrations Only**:
   * When adding new accounts, categories, or settings in future updates, **ALWAYS merge additively**:
     ```javascript
     // Safe non-destructive merge:
     appState.accounts = existingAccounts.concat(newAccountDefaults.filter(n => !existingAccounts.some(e => e.id === n.id)));
     ```
   * Existing balances, transactions, and user-defined goals must be preserved untouched.
3. **Cloud Sync Conflict Protection**:
   * When syncing with the cloud, populated local records must never be replaced with empty remote payloads.
   * Remote timestamps are checked to ensure newer data takes precedence while preventing data loss.
4. **Automatic Version Activation**:
   * When `sw.js` activates a new code version, `window.location.reload()` refreshes the webpage assets while `localStorage` keeps all financial records 100% intact.
