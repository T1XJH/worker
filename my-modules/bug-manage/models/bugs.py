# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bug(models.Model):
    # 类的唯一标志字段，其他类可以通过此字段引用本类
    _name = 'bm.bug'
    # 类似于标签
    _description = 'bug'

    # 该字段是特殊字段，name作为标题，required=True表示为必输字段
    name = fields.Char('bug简述', required=True)
    # 文本字段，size定义其长度为150
    detail = fields.Text()
    # 布尔字段，定义bug是否关闭
    is_closed = fields.Boolean('是否关闭')
    # 关闭理由，Selection可完成列表效果，第一个参数为列表内元素，第二个string属性用于定义字段标签
    close_reason = fields.Selection([('changed', '已修改'), ('cannot', '无法修改'), ('delay', '推迟')], string='关闭理由')
    # 允许选择用户作为bug负责人，多对一关系
    user_id = fields.Many2one('res.users', string='负责人')
    # 允许选择多个关注者，多对多关系
    follower_id = fields.Many2many('res.partner', string='关注者')

    # discovers = fields.Reference(
    #     [('res.user', '用户'),('res.partner', '合作伙伴')],
    #     'bug发现者'
    # )

    # @api.multi
    def do_close(self):
        for item in self:
            item.is_closed = True
        return True

