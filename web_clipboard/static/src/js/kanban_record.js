"use strict";
/**
 * Copyright 2018 Modoolar <info@modoolar.com>
 * License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
 *
 */

odoo.define('web_clipboard.KanbanRecord', function (require) {
    const KanbanRecord = require("web.KanbanRecord");
    const setClipboard = require("web_clipboard.set_clipboard");
    const core = require('web.core');
    const _t = core._t;

    KanbanRecord.include({
        events: Object.assign({}, KanbanRecord.prototype.events, {
            'click [data-copy]': '_onCopyToClipboardClick',
        }),
        _onCopyToClipboardClick(event) {
            event.preventDefault();
            let $button = $(event.currentTarget);
            let copyId = $button.attr("data-copy");
            let $input = this.$("input[data-copy-id='" + copyId + "']");
            setClipboard($input.attr("value"));
            this.do_notify(_t("Copied to clipboard"));
        }
    });
});
