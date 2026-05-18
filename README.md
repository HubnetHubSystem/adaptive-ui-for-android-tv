# Adaptive UI for Android TV / Fire TV

## Problem
Phone apps often don’t work well on Android TV / Fire TV because:
- Screen orientation is locked to portrait
- Touch input expected, but TV uses remote control (DPad)
- UI elements are too small or misplaced

## Solution
App developers should:
1. **Detect the device type** using `UiModeManager` or screen size.
2. **Switch layout** to Leanback (TV) or touch (phone) at runtime.
3. **Support DPad navigation** (focusable buttons, no swipe gestures).
4. **Test on real TV** or emulator with `xlarge` screens.

## Quick checklist
- [ ] Add `android:configChanges="screenSize|orientation"` to manifest.
- [ ] Use different `res/layout` folders: `layout-sw600dp` (phone landscape/small tablet) and `layout-xlarge` (TV).
- [ ] In your main activity, call `UiModeManager.getCurrentModeType()` to check if running on TV.
- [ ] For TV, replace touch listeners with `onClick` and `onFocusChange`.

## Example snippet (Kotlin)
```kotlin
val uiModeManager = getSystemService(UI_MODE_SERVICE) as UiModeManager
if (uiModeManager.currentModeType == Configuration.UI_MODE_TYPE_TELEVISION) {
    // Load TV layout, disable touch-only features
    setContentView(R.layout.activity_tv)
} else {
    setContentView(R.layout.activity_phone)
}
