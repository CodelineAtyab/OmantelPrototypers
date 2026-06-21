import pygame
import sys
import math

# ── palette ────────────────────────────────────────────────
BG          = (10,  13,  26)
SURFACE     = (17,  24,  39)
SURFACE2    = (15,  20,  33)
BORDER      = (30,  45,  69)
BORDER_FOC  = (79, 142, 247)
TEXT        = (226, 232, 240)
MUTED       = (100, 116, 139)
ACCENT      = (79,  142, 247)
ACCENT2     = (167, 139, 250)
SUCCESS     = (52,  211, 153)
DANGER      = (248, 113, 113)
BTN_BG      = (79,  142, 247)
BTN_HOV     = (110, 163, 255)
BTN_TXT     = (255, 255, 255)
ROW_EVEN    = (13,  18,  30)
ROW_ODD     = (17,  24,  39)
ROW_HOVER   = (25,  40,  70)
SCROLLBAR   = (30,  45,  69)
SCROLLTHUMB = (79, 142, 247)

ROW_COLORS = [
    (79,  142, 247),
    (167, 139, 250),
    (52,  211, 153),
    (251, 146,  60),
    (244, 114, 182),
    (250, 204,  21),
]

W, H       = 780, 680
FPS        = 60
RADIUS     = 10
INPUT_H    = 48
BTN_H      = 50
PADDING    = 32
COL_W      = (W - PADDING*2 - 16) // 2


# ── helpers ────────────────────────────────────────────────
def rounded_rect(surf, color,  rect, r=RADIUS, border=0, border_color=None):
    pygame.draw.rect(surf, color, rect, border_radius=r)
    if border and border_color:
        pygame.draw.rect(surf, border_color, rect, border, border_radius=r)

def fmt(n):
    return f"{n:,}"


# ── input widget ───────────────────────────────────────────
class InputBox:
    def __init__(self, x, y, w, h, placeholder="", label=""):
        self.rect       = pygame.Rect(x, y, w, h)
        self.placeholder= placeholder
        self.label      = label
        self.text       = ""
        self.focused    = False
        self.cursor_vis = True
        self.cursor_t   = 0
        self.shake      = 0       # frames of error shake
        self.shake_off  = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.focused = self.rect.collidepoint(event.pos)
        if self.focused and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.lstrip("-").isdigit() or (
                event.unicode == "-" and len(self.text) == 0
            ):
                if len(self.text) < 6:
                    self.text += event.unicode

    def error_shake(self):
        self.shake = 12

    def update(self, dt):
        self.cursor_t += dt
        if self.cursor_t >= 530:
            self.cursor_vis = not self.cursor_vis
            self.cursor_t   = 0
        if self.shake > 0:
            self.shake -= 1
            self.shake_off = int(math.sin(self.shake * 1.2) * 5)
        else:
            self.shake_off = 0

    def draw(self, surf, font_label, font_input):
        rx = self.rect.x + self.shake_off
        # label
        lbl = font_label.render(self.label, True, MUTED)
        surf.blit(lbl, (rx, self.rect.y - 22))
        # box
        border_col = BORDER_FOC if self.focused else BORDER
        rounded_rect(surf, SURFACE2, (rx, self.rect.y, self.rect.w, self.rect.h), RADIUS)
        pygame.draw.rect(surf, border_col,
                         (rx, self.rect.y, self.rect.w, self.rect.h),
                         2, border_radius=RADIUS)
        # text or placeholder
        display = self.text if self.text else self.placeholder
        color   = TEXT if self.text else (*MUTED[:3],)
        tx = font_input.render(display, True, color)
        ty_pos = self.rect.y + (self.rect.h - tx.get_height()) // 2
        surf.blit(tx, (rx + 14, ty_pos))
        # cursor
        if self.focused and self.cursor_vis and self.text:
            cx = rx + 14 + tx.get_width() + 2
            cy = ty_pos + 4
            pygame.draw.line(surf, ACCENT, (cx, cy), (cx, cy + tx.get_height() - 8), 2)

    @property
    def value(self):
        try:    return int(self.text)
        except: return None


# ── button ─────────────────────────────────────────────────
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect    = pygame.Rect(x, y, w, h)
        self.text    = text
        self.hovered = False
        self.pressed = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.pressed = True
            return True
        if event.type == pygame.MOUSEBUTTONUP:
            self.pressed = False
        return False

    def draw(self, surf, font):
        color = BTN_HOV if self.hovered else BTN_BG
        r     = self.rect.inflate(-4, -4) if self.pressed else self.rect
        rounded_rect(surf, color, r, RADIUS)
        lbl = font.render(self.text, True, BTN_TXT)
        surf.blit(lbl, lbl.get_rect(center=r.center))


# ── stat pill ──────────────────────────────────────────────
class StatPill:
    def __init__(self, x, y, w, h, label, color):
        self.rect  = pygame.Rect(x, y, w, h)
        self.label = label
        self.color = color
        self.value = "—"

    def draw(self, surf, font_val, font_lbl):
        rounded_rect(surf, SURFACE2, self.rect, RADIUS)
        pygame.draw.rect(surf, BORDER, self.rect, 1, border_radius=RADIUS)
        # top accent bar
        bar = pygame.Rect(self.rect.x + 16, self.rect.y, self.rect.w - 32, 3)
        pygame.draw.rect(surf, self.color, bar, border_radius=2)
        val = font_val.render(fmt(self.value) if isinstance(self.value, int) else self.value,
                              True, self.color)
        lbl = font_lbl.render(self.label, True, MUTED)
        surf.blit(val, val.get_rect(centerx=self.rect.centerx,
                                    centery=self.rect.centery - 8))
        surf.blit(lbl, lbl.get_rect(centerx=self.rect.centerx,
                                    centery=self.rect.centery + 16))


# ── scrollable table ───────────────────────────────────────
class ResultTable:
    ROW_H    = 40
    HEADER_H = 38

    def __init__(self, x, y, w, h):
        self.rect     = pygame.Rect(x, y, w, h)
        self.rows     = []          # list of (multiplier, number, result)
        self.scroll_y = 0
        self.max_scroll = 0
        self.hovered_row = -1
        self.sb_dragging = False
        self.sb_drag_start = 0
        self.sb_scroll_start = 0

    def set_rows(self, rows):
        self.rows      = rows
        self.scroll_y  = 0
        total_h        = len(rows) * self.ROW_H
        visible_h      = self.rect.h - self.HEADER_H
        self.max_scroll = max(0, total_h - visible_h)

    def _scrollbar_rect(self):
        if self.max_scroll == 0:
            return None
        visible_h = self.rect.h - self.HEADER_H
        total_h   = len(self.rows) * self.ROW_H
        ratio     = visible_h / total_h
        thumb_h   = max(30, int(visible_h * ratio))
        thumb_y   = int((self.scroll_y / self.max_scroll) * (visible_h - thumb_h))
        sb_x = self.rect.right - 10
        return pygame.Rect(sb_x, self.rect.y + self.HEADER_H + thumb_y, 6, thumb_h)

    def handle_event(self, event):
        if event.type == pygame.MOUSEWHEEL and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.scroll_y = max(0, min(self.max_scroll, self.scroll_y - event.y * self.ROW_H))
        if event.type == pygame.MOUSEMOTION:
            mx, my = event.pos
            if self.sb_dragging:
                delta = my - self.sb_drag_start
                visible_h = self.rect.h - self.HEADER_H
                total_h   = len(self.rows) * self.ROW_H
                self.scroll_y = max(0, min(self.max_scroll,
                    self.sb_scroll_start + int(delta * total_h / visible_h)))
            # row hover
            if self.rect.collidepoint(mx, my) and my > self.rect.y + self.HEADER_H:
                rel = my - (self.rect.y + self.HEADER_H) + self.scroll_y
                self.hovered_row = rel // self.ROW_H
            else:
                self.hovered_row = -1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            sb = self._scrollbar_rect()
            if sb and sb.collidepoint(event.pos):
                self.sb_dragging    = True
                self.sb_drag_start  = event.pos[1]
                self.sb_scroll_start = self.scroll_y
        if event.type == pygame.MOUSEBUTTONUP:
            self.sb_dragging = False

    def draw(self, surf, font_hdr, font_row, number):
        # outer box
        rounded_rect(surf, SURFACE, self.rect, RADIUS)
        pygame.draw.rect(surf, BORDER, self.rect, 1, border_radius=RADIUS)

        # header
        hdr_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.HEADER_H)
        rounded_rect(surf, SURFACE2, hdr_rect, RADIUS)
        pygame.draw.line(surf, BORDER,
                         (self.rect.x, self.rect.y + self.HEADER_H),
                         (self.rect.right, self.rect.y + self.HEADER_H), 1)
        cols = [("#", 0.08), ("Expression", 0.42), ("Result", 0.85)]
        for label, frac in cols:
            lx = self.rect.x + int(self.rect.w * frac) + 12
            lt = font_hdr.render(label.upper(), True, MUTED)
            surf.blit(lt, (lx, self.rect.y + (self.HEADER_H - lt.get_height()) // 2))

        # clipping region for rows
        clip = pygame.Rect(self.rect.x, self.rect.y + self.HEADER_H,
                           self.rect.w, self.rect.h - self.HEADER_H)
        old_clip = surf.get_clip()
        surf.set_clip(clip)

        visible_h = self.rect.h - self.HEADER_H
        start_idx = self.scroll_y // self.ROW_H
        end_idx   = min(len(self.rows), start_idx + visible_h // self.ROW_H + 2)

        for i in range(start_idx, end_idx):
            mult, num, result = self.rows[i]
            row_y = self.rect.y + self.HEADER_H + i * self.ROW_H - self.scroll_y

            bg = ROW_HOVER if i == self.hovered_row else (ROW_ODD if i % 2 else ROW_EVEN)
            row_rect = pygame.Rect(self.rect.x + 1, row_y, self.rect.w - 2, self.ROW_H)
            pygame.draw.rect(surf, bg, row_rect)

            color = ROW_COLORS[i % len(ROW_COLORS)]
            cy = row_y + (self.ROW_H - font_row.get_height()) // 2

            # # col
            idx_s  = font_row.render(f"{mult:02d}", True, MUTED)
            surf.blit(idx_s, (self.rect.x + int(self.rect.w * 0.08) + 12, cy))

            # expression col
            expr   = f"{num}  ×  {mult}"
            expr_s = font_row.render(expr, True, TEXT)
            surf.blit(expr_s, (self.rect.x + int(self.rect.w * 0.30) + 12, cy))

            # result col
            res_s  = font_row.render(fmt(result), True, color)
            rx2    = self.rect.right - res_s.get_width() - 28
            surf.blit(res_s, (rx2, cy))

            # separator
            if i < len(self.rows) - 1:
                sep_y = row_y + self.ROW_H - 1
                pygame.draw.line(surf, BORDER,
                                 (self.rect.x + 1, sep_y), (self.rect.right - 1, sep_y), 1)

        surf.set_clip(old_clip)

        # scrollbar track
        if self.max_scroll > 0:
            track = pygame.Rect(self.rect.right - 10,
                                self.rect.y + self.HEADER_H,
                                6,
                                self.rect.h - self.HEADER_H)
            pygame.draw.rect(surf, SCROLLBAR, track, border_radius=3)
            sb = self._scrollbar_rect()
            if sb:
                pygame.draw.rect(surf, SCROLLTHUMB, sb, border_radius=3)


# ── main app ───────────────────────────────────────────────
def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Multiplication Table")
    clock  = pygame.time.Clock()

    # fonts
    mono       = "dejavusansmono"
    f_title    = pygame.font.SysFont(mono, 26, bold=True)
    f_sub      = pygame.font.SysFont(mono, 13)
    f_label    = pygame.font.SysFont(mono, 12, bold=True)
    f_input    = pygame.font.SysFont(mono, 22, bold=True)
    f_btn      = pygame.font.SysFont(mono, 16, bold=True)
    f_stat_val = pygame.font.SysFont(mono, 22, bold=True)
    f_stat_lbl = pygame.font.SysFont(mono, 11, bold=True)
    f_hdr      = pygame.font.SysFont(mono, 11, bold=True)
    f_row      = pygame.font.SysFont(mono, 15, bold=True)
    f_hint     = pygame.font.SysFont(mono, 11)
    f_err      = pygame.font.SysFont(mono, 13)

    # layout constants
    top   = 110          # below header
    inp_y = top + 38

    inp_num = InputBox(PADDING,           inp_y, COL_W, INPUT_H, "e.g.  7",  "NUMBER")
    inp_lim = InputBox(PADDING + COL_W + 16, inp_y, COL_W, INPUT_H, "e.g.  12", "UP TO")
    inp_num.focused = True

    btn_y   = inp_y + INPUT_H + 20
    gen_btn = Button(PADDING, btn_y, W - PADDING*2, BTN_H, "Generate Table   ↵")

    pill_y  = btn_y + BTN_H + 28
    pill_w  = (W - PADDING*2 - 24) // 3
    pills   = [
        StatPill(PADDING,                   pill_y, pill_w, 72, "SMALLEST", ACCENT),
        StatPill(PADDING + pill_w + 12,     pill_y, pill_w, 72, "LARGEST",  ACCENT2),
        StatPill(PADDING + (pill_w + 12)*2, pill_y, pill_w, 72, "SUM",      SUCCESS),
    ]

    tbl_y   = pill_y + 72 + 24
    tbl_h   = H - tbl_y - 40
    table   = ResultTable(PADDING, tbl_y, W - PADDING*2, tbl_h)

    error_msg   = ""
    show_result = False
    inputs      = [inp_num, inp_lim]
    focused_idx = 0

    def do_generate():
        nonlocal error_msg, show_result
        n = inp_num.value
        l = inp_lim.value
        if n is None or l is None:
            error_msg = "⚠  Both fields are required."
            inp_num.error_shake() if n is None else inp_lim.error_shake()
            show_result = False
            return
        if l < 1:
            error_msg = "⚠  'Up to' must be at least 1."
            inp_lim.error_shake()
            show_result = False
            return
        if l > 500:
            error_msg = "⚠  'Up to' cannot exceed 500."
            inp_lim.error_shake()
            show_result = False
            return
        error_msg = ""
        rows = [(i, n, n * i) for i in range(1, l + 1)]
        table.set_rows(rows)
        pills[0].value = rows[0][2]
        pills[1].value = rows[-1][2]
        pills[2].value = sum(r for _, _, r in rows)
        show_result = True

    running = True
    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    do_generate()
                elif event.key == pygame.K_TAB:
                    focused_idx = (focused_idx + 1) % 2
                    inputs[0].focused = (focused_idx == 0)
                    inputs[1].focused = (focused_idx == 1)
                elif event.key == pygame.K_ESCAPE:
                    running = False

            for inp in inputs:
                inp.handle_event(event)
            gen_btn.handle_event(event)
            if gen_btn.handle_event(event):
                do_generate()
            if show_result:
                table.handle_event(event)

        for inp in inputs:
            inp.update(dt)

        # ── draw ──
        screen.fill(BG)

        # title
        title = f_title.render("✦  Multiply  Anything", True, ACCENT)
        screen.blit(title, title.get_rect(centerx=W//2, y=28))
        sub = f_sub.render("enter a number and a limit, then press Enter", True, MUTED)
        screen.blit(sub, sub.get_rect(centerx=W//2, y=66))

        # divider
        pygame.draw.line(screen, BORDER, (PADDING, top - 6), (W - PADDING, top - 6), 1)

        # inputs
        inp_num.draw(screen, f_label, f_input)
        inp_lim.draw(screen, f_label, f_input)

        # button
        gen_btn.draw(screen, f_btn)

        # error
        if error_msg:
            em = f_err.render(error_msg, True, DANGER)
            screen.blit(em, em.get_rect(centerx=W//2, y=btn_y + BTN_H + 8))

        # pills + table
        if show_result:
            for p in pills:
                p.draw(screen, f_stat_val, f_stat_lbl)
            n = inp_num.value
            table.draw(screen, f_hdr, f_row, n)

        # hint
        hint = f_hint.render("Tab — switch field   ·   Enter — generate   ·   Esc — quit", True, (*MUTED, 160))
        screen.blit(hint, hint.get_rect(centerx=W//2, y=H - 22))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()