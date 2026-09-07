# -*- coding: utf-8 -*-
"""Stylised product screens, one per case study.

The reference sites this was measured against carry their visual weight with
real product screenshots. There are no real products here yet, and inventing a
screenshot of a client app would be dishonest, so each case study gets a
deliberately stylised mock-up instead: plain elements built from the site's own
colour tokens, so they theme with everything else and read as a diagram of the
screen rather than a photograph of one.

Every mock is decorative — the pages mark them aria-hidden and the text says
everything the picture does.
"""


def _lines(n, widths):
    return "".join('<i class="mk-line" style="width:%s"></i>' % widths[i % len(widths)]
                   for i in range(n))


PHONE_ORDER = '''<div class="mock mock--phone">
  <div class="mock__notch"></div>
  <div class="mock__body">
    <div class="mk-head"><i class="mk-line mk-line--title" style="width:58%"></i></div>
    <div class="mk-steps">
      <span class="mk-step is-done"></span><span class="mk-rail is-done"></span>
      <span class="mk-step is-done"></span><span class="mk-rail is-done"></span>
      <span class="mk-step is-now"></span><span class="mk-rail"></span>
      <span class="mk-step"></span>
    </div>
    <p class="mk-cap">Out for delivery</p>
    <div class="mk-list">
      <div class="mk-item"><i class="mk-sq"></i><i class="mk-line" style="width:52%"></i><b class="mk-num"></b></div>
      <div class="mk-item"><i class="mk-sq"></i><i class="mk-line" style="width:64%"></i><b class="mk-num"></b></div>
      <div class="mk-item"><i class="mk-sq"></i><i class="mk-line" style="width:44%"></i><b class="mk-num"></b></div>
    </div>
    <div class="mk-total"><i class="mk-line" style="width:34%"></i><b class="mk-num mk-num--wide"></b></div>
    <div class="mk-btn"></div>
  </div>
</div>'''

DASH_COACHING = '''<div class="mock">
  <div class="mock__bar"><i></i><i></i><i></i></div>
  <div class="mock__split">
    <div class="mk-side">
      <i class="mk-side__row is-on"></i><i class="mk-side__row"></i>
      <i class="mk-side__row"></i><i class="mk-side__row"></i>
    </div>
    <div class="mock__body">
      <div class="mk-tiles mk-tiles--3">
        <div class="mk-tile"><b></b><i class="mk-line" style="width:70%"></i></div>
        <div class="mk-tile"><b></b><i class="mk-line" style="width:56%"></i></div>
        <div class="mk-tile"><b></b><i class="mk-line" style="width:64%"></i></div>
      </div>
      <div class="mk-table">
        <div class="mk-tr mk-tr--head"><i style="width:38%"></i><i style="width:22%"></i><i style="width:18%"></i></div>
        <div class="mk-tr"><i style="width:44%"></i><i style="width:20%"></i><span class="mk-tag mk-tag--ok"></span></div>
        <div class="mk-tr"><i style="width:36%"></i><i style="width:26%"></i><span class="mk-tag mk-tag--ok"></span></div>
        <div class="mk-tr"><i style="width:50%"></i><i style="width:18%"></i><span class="mk-tag mk-tag--warn"></span></div>
        <div class="mk-tr"><i style="width:40%"></i><i style="width:24%"></i><span class="mk-tag mk-tag--ok"></span></div>
      </div>
    </div>
  </div>
</div>'''

DASH_AUTOMATION = '''<div class="mock">
  <div class="mock__bar"><i></i><i></i><i></i></div>
  <div class="mock__body">
    <div class="mk-tiles mk-tiles--3">
      <div class="mk-tile"><b></b><i class="mk-line" style="width:64%"></i></div>
      <div class="mk-tile"><b></b><i class="mk-line" style="width:52%"></i></div>
      <div class="mk-tile"><b></b><i class="mk-line" style="width:72%"></i></div>
    </div>
    <div class="mk-chart">
      <span style="--h:38%"></span><span style="--h:62%"></span><span style="--h:47%"></span>
      <span style="--h:80%"></span><span style="--h:58%"></span><span style="--h:92%"></span>
      <span style="--h:70%"></span>
    </div>
    <div class="mk-alert"><i class="mk-dot"></i><i class="mk-line" style="width:62%"></i></div>
  </div>
</div>'''

PORTAL_ESTATE = '''<div class="mock">
  <div class="mock__bar"><i></i><i></i><i></i></div>
  <div class="mock__body">
    <div class="mk-search"><i class="mk-line" style="width:46%"></i><span class="mk-btn mk-btn--sm"></span></div>
    <div class="mk-tiles mk-tiles--3">
      <div class="mk-prop"><span class="mk-photo"></span><i class="mk-line" style="width:80%"></i><i class="mk-line mk-line--fade" style="width:56%"></i></div>
      <div class="mk-prop"><span class="mk-photo"></span><i class="mk-line" style="width:68%"></i><i class="mk-line mk-line--fade" style="width:62%"></i></div>
      <div class="mk-prop"><span class="mk-photo"></span><i class="mk-line" style="width:74%"></i><i class="mk-line mk-line--fade" style="width:48%"></i></div>
    </div>
    <div class="mk-table">
      <div class="mk-tr"><i style="width:40%"></i><span class="mk-tag mk-tag--ok"></span></div>
      <div class="mk-tr"><i style="width:52%"></i><span class="mk-tag mk-tag--warn"></span></div>
    </div>
  </div>
</div>'''

PHONE_DELIVERY = '''<div class="mock mock--phone">
  <div class="mock__notch"></div>
  <div class="mock__body">
    <div class="mk-map">
      <svg viewBox="0 0 200 150" fill="none" stroke="currentColor" stroke-width="2.4"
           stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path class="mk-route" d="M22 126c26-4 30-38 56-44s34-26 60-30 30-14 40-16"/>
        <path d="M12 40h48M12 62h26M150 118h38M126 136h62" class="mk-grid-line"/>
      </svg>
      <span class="mk-pin mk-pin--a"></span>
      <span class="mk-pin mk-pin--b"></span>
    </div>
    <div class="mk-driver">
      <i class="mk-avatar"></i>
      <span><i class="mk-line" style="width:70%"></i><i class="mk-line mk-line--fade" style="width:46%"></i></span>
    </div>
    <div class="mk-total"><i class="mk-line" style="width:40%"></i><b class="mk-num mk-num--wide"></b></div>
  </div>
</div>'''

CAL_BOOKING = '''<div class="mock">
  <div class="mock__bar"><i></i><i></i><i></i></div>
  <div class="mock__body">
    <div class="mk-head"><i class="mk-line mk-line--title" style="width:42%"></i></div>
    <div class="mk-week">
      <i></i><i></i><i></i><i></i><i></i>
    </div>
    <div class="mk-slots">
      <span class="is-taken"></span><span></span><span class="is-taken"></span><span></span><span></span>
      <span></span><span class="is-taken"></span><span></span><span class="is-taken"></span><span></span>
      <span class="is-taken"></span><span></span><span></span><span></span><span class="is-taken"></span>
      <span></span><span></span><span class="is-taken"></span><span></span><span></span>
    </div>
    <div class="mk-btn"></div>
  </div>
</div>'''

MOCKS = {
    "restaurant-ordering-app": PHONE_ORDER,
    "coaching-management-platform": DASH_COACHING,
    "business-automation-dashboard": DASH_AUTOMATION,
    "real-estate-listing-portal": PORTAL_ESTATE,
    "delivery-tracking-app": PHONE_DELIVERY,
    "booking-and-scheduling-mvp": CAL_BOOKING,
}


def mock_for(slug, bare=False):
    """Return one screen.

    `bare` skips the surrounding panel, for callers that already draw one —
    otherwise the screen sits inside two nested boxes and cannot fill either.
    """
    html = MOCKS.get(slug, DASH_AUTOMATION)
    if bare:
        return '<div class="mockbare" aria-hidden="true">\n%s\n</div>' % html
    return '<div class="mockwrap" aria-hidden="true">\n%s\n</div>' % html
