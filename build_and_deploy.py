#!/usr/bin/env python3
import os
import re

DIR = '/Users/sithu/Downloads/n8n/money-manager'

with open(os.path.join(DIR, 'tailwind.min.css'), 'r', encoding='utf-8') as f:
    tailwind_css = f.read()

with open(os.path.join(DIR, 'lucide.min.js'), 'r', encoding='utf-8') as f:
    lucide_js = f.read()

with open(os.path.join(DIR, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inline tailwind.min.css into <head>
tailwind_tag = '<link rel="stylesheet" href="tailwind.min.css">'
inlined_tw = f'<style id="inlined-tailwind-css">\n{tailwind_css}\n</style>'
if tailwind_tag in html:
    html = html.replace(tailwind_tag, inlined_tw)

# 2. Modernize Gold CSS Classes to Sapphire Obsidian & Mint Emerald
old_gold_css = """    /* 24K VIP Gold Styling */
    .gold-gradient-text {
      background: linear-gradient(135deg, #FFFDF0 0%, #FDE68A 30%, #F59E0B 75%, #D97706 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .gold-card {
      background: linear-gradient(145deg, rgba(245, 158, 11, 0.08) 0%, rgba(26, 22, 16, 0.82) 40%, rgba(18, 20, 28, 0.96) 100%);
      border: 1px solid rgba(245, 158, 11, 0.28);
      box-shadow: inset 0 1px 1px rgba(253, 230, 138, 0.15), 0 20px 40px -15px rgba(0, 0, 0, 0.85);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .gold-card:hover {
      border-color: rgba(251, 191, 36, 0.5);
      box-shadow: inset 0 1px 2px rgba(253, 230, 138, 0.25), 0 20px 45px -10px rgba(245, 158, 11, 0.18);
      transform: translateY(-2px);
    }
    .gold-card-achieved {
      background: linear-gradient(145deg, rgba(245, 158, 11, 0.18) 0%, rgba(38, 30, 15, 0.9) 45%, rgba(18, 20, 28, 0.98) 100%);
      border: 1.5px solid rgba(251, 191, 36, 0.65);
      box-shadow: inset 0 1px 2px rgba(253, 230, 138, 0.4), 0 0 35px rgba(245, 158, 11, 0.25);
    }
    .gold-btn {
      background: linear-gradient(135deg, #FEF08A 0%, #F59E0B 50%, #D97706 100%);
      color: #171003 !important;
      font-weight: 800;
      box-shadow: 0 4px 18px rgba(245, 158, 11, 0.35);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .gold-btn:hover {
      background: linear-gradient(135deg, #FFFFFF 0%, #FBBF24 50%, #D97706 100%);
      box-shadow: 0 6px 24px rgba(245, 158, 11, 0.55);
      transform: translateY(-1px);
    }
    .gold-btn:active {
      transform: translateY(1px) scale(0.97);
    }"""

new_sapphire_css = """    /* Precision Modern Sapphire Vault & Clean Fintech Styling */
    .gold-gradient-text, .vault-gradient-text {
      background: linear-gradient(135deg, #FFFFFF 0%, #38BDF8 50%, #34D399 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .gold-card, .vault-card {
      background: linear-gradient(145deg, rgba(56, 189, 248, 0.08) 0%, rgba(15, 23, 42, 0.88) 40%, rgba(10, 15, 29, 0.96) 100%);
      border: 1px solid rgba(56, 189, 248, 0.28);
      box-shadow: inset 0 1px 1px rgba(224, 242, 254, 0.15), 0 20px 40px -15px rgba(0, 0, 0, 0.85);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .gold-card:hover, .vault-card:hover {
      border-color: rgba(56, 189, 248, 0.55);
      box-shadow: inset 0 1px 2px rgba(224, 242, 254, 0.25), 0 20px 45px -10px rgba(56, 189, 248, 0.2);
      transform: translateY(-2px);
    }
    .gold-card-achieved, .vault-card-achieved {
      background: linear-gradient(145deg, rgba(16, 185, 129, 0.16) 0%, rgba(6, 78, 59, 0.5) 45%, rgba(10, 15, 29, 0.98) 100%);
      border: 1.5px solid rgba(52, 211, 153, 0.65);
      box-shadow: inset 0 1px 2px rgba(167, 243, 208, 0.4), 0 0 35px rgba(16, 185, 129, 0.25);
    }
    .gold-btn, .vault-btn {
      background: linear-gradient(135deg, #38BDF8 0%, #2563EB 60%, #1D4ED8 100%);
      color: #FFFFFF !important;
      font-weight: 800;
      box-shadow: 0 4px 18px rgba(37, 99, 235, 0.35);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .gold-btn:hover, .vault-btn:hover {
      background: linear-gradient(135deg, #7DD3FC 0%, #3B82F6 60%, #1D4ED8 100%);
      box-shadow: 0 6px 24px rgba(37, 99, 235, 0.55);
      transform: translateY(-1px);
    }
    .gold-btn:active, .vault-btn:active {
      transform: translateY(1px) scale(0.97);
    }"""

if old_gold_css in html:
    html = html.replace(old_gold_css, new_sapphire_css)

# 3. Add In-App WhatsApp/Messenger Safari Helper Banner right after <body>
body_open = '<body class="min-h-screen text-slate-100 flex flex-col font-sans selection:bg-indigo-500/30 selection:text-white pb-24 sm:pb-8">'
inapp_banner = """<body class="min-h-screen text-slate-100 flex flex-col font-sans selection:bg-indigo-500/30 selection:text-white pb-24 sm:pb-8">

  <!-- WhatsApp / In-App Browser Detection Alert Bar -->
  <div id="inapp-safari-banner" class="hidden sticky top-0 z-[150] w-full bg-gradient-to-r from-blue-600 via-indigo-600 to-sky-500 text-white px-3 py-2 text-xs flex items-center justify-between shadow-lg">
    <div class="flex items-center gap-2">
      <i data-lucide="compass" class="w-4 h-4 shrink-0 text-cyan-200 animate-spin" style="animation-duration: 8s;"></i>
      <span class="font-bold text-[11px] leading-tight">iPhone စခရင်ပေါ် App အဖြစ် တင်သုံးရန် Safari ဖြင့် ဖွင့်ပါ</span>
    </div>
    <button type="button" onclick="copyAppUrlForSafari()" class="px-2.5 py-1 bg-white text-slate-900 rounded-full font-black text-[10px] shrink-0 active:scale-95 shadow cursor-pointer">
      Safari Link ကူးမည်
    </button>
  </div>"""

if body_open in html and 'inapp-safari-banner' not in html:
    html = html.replace(body_open, inapp_banner)

# 4. Update Goals Header from "24K VIP Gold Vault" to "💎 Sapphire Wealth Vault"
html = html.replace(
    '<span class="text-xs font-black tracking-widest text-amber-200 uppercase">24K VIP Gold Vault</span>',
    '<span class="text-xs font-black tracking-widest text-cyan-200 uppercase">💎 Sapphire Wealth Vault</span>'
)
html = html.replace(
    '<p class="text-xs text-amber-200/80 font-medium">Personal Wealth Milestones & Vault Storage</p>',
    '<p class="text-xs text-cyan-200/80 font-medium">Personal Wealth Milestones & Savings Vault</p>'
)
html = html.replace(
    'bg-amber-500/20 border border-amber-400/40',
    'bg-sky-500/20 border border-sky-400/40'
)

# 5. Fix #pwa-install-modal: Remove mobileconfig, Add clear iOS guidance and Android APK
old_ios_install_view = """      <!-- iOS Installation Steps View -->
      <div id="install-view-ios" class="space-y-2.5 text-xs text-slate-300 text-left leading-relaxed">
        <!-- Direct iPhone Profile Download Button -->
        <a href="BurmeseMoneyManager.mobileconfig" download="BurmeseMoneyManager.mobileconfig" onclick="showToast('🍏 iPhone ပရိုဖိုင် ဒေါင်းလုဒ်ပြီးပါက Settings > Profile Downloaded > Install နှိပ်ပါ')" class="w-full py-3 px-4 rounded-2xl bg-gradient-to-r from-sky-500 to-blue-600 hover:from-sky-400 hover:to-blue-500 text-white font-black text-xs flex items-center justify-center gap-2 shadow-lg shadow-sky-500/25 transition btn-press cursor-pointer">
          <i data-lucide="download" class="w-4 h-4 text-white"></i>
          <span>📲 iPhone App ပရိုဖိုင် ဒေါင်းလုဒ် (.mobileconfig)</span>
        </a>

        <div class="flex items-start gap-2.5 p-3 rounded-2xl bg-white/[0.04] border border-white/5">
          <span class="w-6 h-6 rounded-full bg-cyan-500 text-slate-950 flex items-center justify-center text-xs font-black shrink-0">1</span>
          <div>
            <p class="font-bold text-white">Safari အောက်ခြေရှိ Share ခလုတ်ကို နှိပ်ပါ</p>
            <p class="text-[10px] text-slate-400 mt-0.5">Safari ၏ အောက်ဘက် မီနူးဘားရှိ <b>[ <i data-lucide="share" class="w-3 h-3 inline text-indigo-400"></i> Share ]</b> အိုင်ကွန်ကို နှိပ်ပါ</p>
          </div>
        </div>
        <div class="flex items-start gap-2.5 p-3 rounded-2xl bg-white/[0.04] border border-white/5">
          <span class="w-6 h-6 rounded-full bg-cyan-500 text-slate-950 flex items-center justify-center text-xs font-black shrink-0">2</span>
          <div>
            <p class="font-bold text-white">"Add to Home Screen" ကို ရွေးပါ</p>
            <p class="text-[10px] text-slate-400 mt-0.5">ပေါ်လာသောစာရင်းကို အောက်ဆွဲချပြီး <b>[ ⊞ Add to Home Screen (ပင်မမျက်နှာပြင်သို့ ထည့်မည်) ]</b> ကို နှိပ်ပါ</p>
          </div>
        </div>
        <div class="flex items-start gap-2.5 p-3 rounded-2xl bg-white/[0.04] border border-white/5">
          <span class="w-6 h-6 rounded-full bg-cyan-500 text-slate-950 flex items-center justify-center text-xs font-black shrink-0">3</span>
          <div>
            <p class="font-bold text-white">အပေါ်ညာဘက်ရှိ "Add" ကို နှိပ်ပါ</p>
            <p class="text-[10px] text-slate-400 mt-0.5">သင့် iPhone ပင်မစခရင်ပေါ်တွင် App Icon ရရှိပြီး ဒေါင်းလုဒ်ဖိုင်ထဲ လိုက်ရှာစရာမလိုဘဲ အချိန်မရွေး တိုက်ရိုက် သုံးနိုင်ပါပြီ</p>
          </div>
        </div>
      </div>"""

new_ios_install_view = """      <!-- iOS Installation Steps View -->
      <div id="install-view-ios" class="space-y-2.5 text-xs text-slate-300 text-left leading-relaxed">
        <!-- iOS Notice Box -->
        <div class="p-3.5 rounded-2xl bg-sky-500/10 border border-sky-500/20 space-y-1">
          <div class="flex items-center gap-2 text-sky-300 font-bold text-xs">
            <i data-lucide="info" class="w-4 h-4 shrink-0 text-sky-400"></i>
            <span>iPhone ပေါ်တွင် App အဖြစ် အမြဲတမ်း သွင်းယူနည်း</span>
          </div>
          <p class="text-[11px] text-slate-300 leading-relaxed">
            Apple ၏ လုံခြုံရေးစည်းမျဉ်းအရ iPhone တွင် .apk ကဲ့သို့ ဖိုင်ဒေါင်းလုဒ်ဆွဲ၍ Install လုပ်ခွင့်မပြုပါ။ <b>Safari ဘရောက်ဇာ</b> မှတစ်ဆင့် အောက်ပါ ၃ ဆင့်ဖြင့် သင့် iPhone စခရင်ပေါ်တွင် App အစစ်အတိုင်း တိုက်ရိုက် တင်သုံးနိုင်ပါသည် -
          </p>
        </div>

        <!-- WhatsApp In-App Warning & Copy Link -->
        <div id="ios-whatsapp-tip" class="hidden p-3 rounded-2xl bg-amber-500/15 border border-amber-500/30 space-y-2">
          <p class="text-[11px] text-amber-200 font-bold leading-tight">
            ⚠️ WhatsApp (သို့) Messenger အတွင်းမှ ဖွင့်ထားပါက Apple စည်းမျဉ်းအရ "Add to Home Screen" မပေါ်ပါ။ Safari ဖြင့် ဖွင့်ရပါမည်။
          </p>
          <button type="button" onclick="copyAppUrlForSafari()" class="w-full py-2 px-3 rounded-xl bg-white text-slate-900 font-black text-xs flex items-center justify-center gap-1.5 shadow transition btn-press cursor-pointer">
            <i data-lucide="copy" class="w-3.5 h-3.5"></i>
            <span>Safari တွင် ဖွင့်ရန် Link ကူးယူမည်</span>
          </button>
        </div>

        <div class="flex items-start gap-2.5 p-3 rounded-2xl bg-white/[0.04] border border-white/5">
          <span class="w-6 h-6 rounded-full bg-cyan-500 text-slate-950 flex items-center justify-center text-xs font-black shrink-0">1</span>
          <div>
            <p class="font-bold text-white">Safari အောက်ခြေရှိ [ Share ] ခလုတ်ကို နှိပ်ပါ</p>
            <p class="text-[10px] text-slate-400 mt-0.5">Safari ၏ အောက်ဘက် မီနူးဘားရှိ <b>[ <i data-lucide="share" class="w-3 h-3 inline text-cyan-400"></i> Share ]</b> အိုင်ကွန်ကို နှိပ်ပါ</p>
          </div>
        </div>
        <div class="flex items-start gap-2.5 p-3 rounded-2xl bg-white/[0.04] border border-white/5">
          <span class="w-6 h-6 rounded-full bg-cyan-500 text-slate-950 flex items-center justify-center text-xs font-black shrink-0">2</span>
          <div>
            <p class="font-bold text-white">"Add to Home Screen" ကို ရွေးပါ</p>
            <p class="text-[10px] text-slate-400 mt-0.5">ပေါ်လာသောစာရင်းကို အောက်ဆွဲချပြီး <b>[ ⊞ Add to Home Screen (ပင်မမျက်နှာပြင်သို့ ထည့်မည်) ]</b> ကို နှိပ်ပါ</p>
          </div>
        </div>
        <div class="flex items-start gap-2.5 p-3 rounded-2xl bg-white/[0.04] border border-white/5">
          <span class="w-6 h-6 rounded-full bg-cyan-500 text-slate-950 flex items-center justify-center text-xs font-black shrink-0">3</span>
          <div>
            <p class="font-bold text-white">အပေါ်ညာဘက်ရှိ "Add" ကို နှိပ်ပါ</p>
            <p class="text-[10px] text-slate-400 mt-0.5">သင့် iPhone ပင်မစခရင်ပေါ်တွင် App Icon ရရှိပြီး အင်တာနက်မရှိချိန် (Offline) ပါ App အစစ်အတိုင်း တိုက်ရိုက် သုံးနိုင်ပါပြီ</p>
          </div>
        </div>

        <!-- 1-Click Copy Link Button for Safari -->
        <button type="button" onclick="copyAppUrlForSafari()" class="w-full py-2.5 px-3 rounded-xl bg-white/10 hover:bg-white/15 text-white font-bold text-xs flex items-center justify-center gap-1.5 transition btn-press cursor-pointer">
          <i data-lucide="external-link" class="w-3.5 h-3.5 text-cyan-400"></i>
          <span>Safari တွင် Paste လုပ်ရန် Link ကူးယူမည်</span>
        </button>
      </div>"""

if old_ios_install_view in html:
    html = html.replace(old_ios_install_view, new_ios_install_view)

# 6. Update #auth-gateway buttons: Remove mobileconfig, Add clear buttons
old_auth_bottom = """        <!-- 6. Direct Mobile App Download Options (iOS & Android) -->
        <div class="pt-2 border-t border-white/[0.08] space-y-2 text-left">
          <p class="text-[10px] text-slate-400 font-bold uppercase tracking-wider text-center">ဖုန်းထဲသို့ Application အဖြစ် တိုက်ရိုက်သွင်းယူရန်</p>
          <div class="grid grid-cols-2 gap-2">
            <!-- iOS Button: Direct .mobileconfig Profile Download -->
            <a href="BurmeseMoneyManager.mobileconfig" download="BurmeseMoneyManager.mobileconfig" onclick="showToast('🍏 iPhone ပရိုဖိုင် ဒေါင်းလုဒ်ပြီးပါက Settings > Profile Downloaded > Install နှိပ်ပါ')" class="py-2.5 px-2 rounded-xl bg-sky-500/10 hover:bg-sky-500/20 text-sky-300 border border-sky-500/30 font-bold text-[10px] flex items-center justify-center gap-1.5 transition btn-press cursor-pointer text-center">
              <i data-lucide="apple" class="w-3.5 h-3.5 text-sky-400"></i>
              <span>iPhone App (.mobileconfig)</span>
            </a>
            <!-- Android Button: Direct .apk Download -->
            <a href="BurmeseMoneyManager.apk" download="BurmeseMoneyManager.apk" onclick="showToast('🤖 Android APK အား စတင်ဒေါင်းလုဒ်ဆွဲနေပါပြီ...')" class="py-2.5 px-2 rounded-xl bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold text-[10px] flex items-center justify-center gap-1.5 transition btn-press cursor-pointer text-center">
              <i data-lucide="smartphone" class="w-3.5 h-3.5 text-emerald-400"></i>
              <span>Android App (.apk)</span>
            </a>
          </div>
        </div>"""

new_auth_bottom = """        <!-- 6. Direct Mobile App Download Options (iOS & Android) -->
        <div class="pt-2 border-t border-white/[0.08] space-y-2 text-left">
          <p class="text-[10px] text-slate-400 font-bold uppercase tracking-wider text-center">ဖုန်းထဲသို့ Application အဖြစ် တိုက်ရိုက်သွင်းယူရန်</p>
          <div class="grid grid-cols-2 gap-2">
            <!-- iOS Button -->
            <button type="button" onclick="openPhoneInstallModal('ios')" class="py-2.5 px-2 rounded-xl bg-sky-500/10 hover:bg-sky-500/20 text-sky-300 border border-sky-500/30 font-bold text-[10px] flex items-center justify-center gap-1.5 transition btn-press cursor-pointer text-center">
              <i data-lucide="apple" class="w-3.5 h-3.5 text-sky-400"></i>
              <span>iPhone App သွင်းနည်း</span>
            </button>
            <!-- Android Button: Direct .apk Download -->
            <a href="BurmeseMoneyManager.apk" download="BurmeseMoneyManager.apk" onclick="showToast('🤖 Android APK အား စတင်ဒေါင်းလုဒ်ဆွဲနေပါပြီ...')" class="py-2.5 px-2 rounded-xl bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold text-[10px] flex items-center justify-center gap-1.5 transition btn-press cursor-pointer text-center">
              <i data-lucide="smartphone" class="w-3.5 h-3.5 text-emerald-400"></i>
              <span>Android App (.apk)</span>
            </a>
          </div>
        </div>"""

if old_auth_bottom in html:
    html = html.replace(old_auth_bottom, new_auth_bottom)

# 7. Update initApp to auto-login as guest for first-time visitors
old_init_auth = """      const activeUserId = localStorage.getItem(ACTIVE_SESSION_KEY);
      if (activeUserId) {
        loadUserSession(activeUserId);
        hideAuthGateway();
      } else {
        showAuthGateway();
      }"""

new_init_auth = """      const activeUserId = localStorage.getItem(ACTIVE_SESSION_KEY);
      if (activeUserId) {
        loadUserSession(activeUserId);
        hideAuthGateway();
      } else {
        // Auto-start Guest session so users are never blocked
        handleLoginAsGuest();
      }
      checkInAppBrowser();"""

if old_init_auth in html:
    html = html.replace(old_init_auth, new_init_auth)

# 8. Add checkInAppBrowser & copyAppUrlForSafari functions
helper_js = """
    function checkInAppBrowser() {
      const ua = navigator.userAgent || navigator.vendor || window.opera || '';
      const isIOS = /iPad|iPhone|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
      const isInApp = /FBAN|FBAV|Instagram|WhatsApp|Line|Messenger|MicroMessenger/i.test(ua);
      
      const inAppBanner = document.getElementById('inapp-safari-banner');
      const whatsAppTip = document.getElementById('ios-whatsapp-tip');
      
      if (isIOS && isInApp) {
        if (inAppBanner) {
          inAppBanner.classList.remove('hidden');
          inAppBanner.classList.add('flex');
        }
        if (whatsAppTip) {
          whatsAppTip.classList.remove('hidden');
        }
      }
    }

    function copyAppUrlForSafari() {
      const url = 'https://burmese-money-manager.surge.sh';
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(() => {
          showToast('📋 Link ကူးယူပြီးပါပြီ! Safari တွင် ဖွင့်ပါ');
          alert('Link ကူးယူပြီးပါပြီ!\\n\\n1. iPhone ၏ "Safari" ဘရောက်ဇာကို ဖွင့်ပါ\\n2. Address bar တွင် Paste လုပ်ပြီး ဝင်ရောက်ပါ\\n3. အောက်ခြေရှိ Share ခလုတ်မှတစ်ဆင့် "Add to Home Screen" ကို နှိပ်ပါက ဖုန်းစခရင်ပေါ်တွင် App တိုက်ရိုက် ရောက်ရှိသွားပါမည်။');
        }).catch(() => {
          prompt('Safari တွင် ဖွင့်ရန် ဤ Link ကို ကူးယူပါ:', url);
        });
      } else {
        prompt('Safari တွင် ဖွင့်ရန် ဤ Link ကို ကူးယူပါ:', url);
      }
    }
"""

if 'function checkInAppBrowser' not in html:
    html = html.replace('function openPhoneInstallModal() {', helper_js + '\n    function openPhoneInstallModal(preferredOS) {')
    html = html.replace("const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;\n      switchInstallOSTab(isIOS ? 'ios' : 'android');",
                        "const isIOS = preferredOS ? (preferredOS === 'ios') : (/iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream);\n      switchInstallOSTab(isIOS ? 'ios' : 'android');")

# 9. Clean up preset avatars: replace gold_crest with sapphire_shield
old_avatar = """      { id: 'gold_crest', name: 'VIP Gold', src: "data:image/svg+xml;utf8," + encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="50" fill="#181308"/><circle cx="50" cy="50" r="44" stroke="#F59E0B" stroke-width="2" fill="none"/><polygon points="50,24 60,42 80,45 65,60 69,80 50,70 31,80 35,60 20,45 40,42" fill="#FBBF24"/></svg>`) },"""
new_avatar = """      { id: 'sapphire_shield', name: 'Sapphire Shield', src: "data:image/svg+xml;utf8," + encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="50" fill="#0B132B"/><circle cx="50" cy="50" r="44" stroke="#38BDF8" stroke-width="2.5" fill="none"/><path d="M50,22 L72,34 L72,58 C72,72 50,82 50,82 C50,82 28,72 28,58 L28,34 Z" fill="#0284C7"/><path d="M50,28 L66,38 L66,56 C66,66 50,74 50,74 C50,74 34,66 34,56 L34,38 Z" fill="#38BDF8"/></svg>`) },"""

if old_avatar in html:
    html = html.replace(old_avatar, new_avatar)

# 10. Update wallpaper preset
html = html.replace(
    "id: 'preset_gold', \n        name_my: '24K VIP Gold (ရွှေရောင်ဆန်း)', \n        name_en: '24K Champagne Gold'",
    "id: 'preset_sapphire', \n        name_my: 'Sapphire Obsidian (ခေတ်မီဆန်းသစ်)', \n        name_en: 'Sapphire Cyber Titanium'"
)

# Write updated index.html
with open(os.path.join(DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully! Size:", len(html))

# Also create updated Burmese-Money-Manager.html with inlined lucide.min.js
standalone_html = html.replace(
    '<script src="lucide.min.js"></script>',
    f'<script>\n{lucide_js}\n</script>'
)
with open(os.path.join(DIR, 'Burmese-Money-Manager.html'), 'w', encoding='utf-8') as f:
    f.write(standalone_html)

print("Updated Burmese-Money-Manager.html successfully! Size:", len(standalone_html))
