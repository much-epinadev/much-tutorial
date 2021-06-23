odoo.define('my_field_widget', function (require) {
    "use strict";

    const AbstractField = require('web.AbstractField');
    const fieldRegistry = require('web.field_registry');
    const core = require('web.core')
    const qweb = core.qweb;

    const colorField = AbstractField.extend({
        className: 'o_int_colorpicker',
        tagName: 'span',
        supportedFieldTypes: ['integer'],
        events: {
            'click .o_color_pill': 'clickPill',
        },
        xmlDependencies: ['election/static/src/xml/qweb_template.xml'],
        init: function () {
            this.totalColors = 10;
            this._super.apply(this, arguments);
        },
        _renderEdit: function () {
            this.$el.empty();
            const pills = qweb.render('FieldColorPills', { widget: this })

            this.$el.append(pills)
        },
        _renderReadonly: function () {
            const className = `o_color_pill active readonly o_color_${this.value}`;
            this.$el.append($('<span>', { 'class': className }));
        },
        clickPill: function (ev) {
            var $target = $(ev.currentTarget);
            var data = $target.data();
            this._setValue(data.val.toString());
        }

    });

    fieldRegistry.add('badge_color_widget', colorField);

    return {
        colorField: colorField,
    };
});