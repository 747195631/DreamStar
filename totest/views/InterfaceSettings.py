#!/usr/bin/env python
# coding=utf-8
###########################################
# File: InterfaceSettingsTreegrid.py
# Desc: 接口设置视图层
# Author: 张羽锋
# History: 2016/01/01 张羽锋 新建
###########################################

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from totest.models import HttpInterfaceInfo
import simplejson
from django.http.response import HttpResponse
import uuid
import logging

logger = logging.getLogger("DreamStar.app")


# 功能菜单-测试接口设置视图接口
def interface_settings_treegrid(request):
    try:
        # context_instance=RequestContext(request)进行csrf认证
        return render_to_response("interfaceSettingsTreegrid.html", context_instance=RequestContext(request))
    except Exception as e:
        logger.error(e)
        logger.exception(u"测试接口设置页面错误如下:")


# 功能菜单-测试接口设置数据接口
def interface_settings_json_response(request):
    try:
        paging_data = request.GET
        logger.info("请求的分页要求数据信息paging_data=" + str(paging_data))
        page = paging_data.get("page")
        logger.info("当前页page=" + str(page))
        rows = paging_data.get("rows")
        logger.info("每页显示行数rows=" + str(rows))
        interface_settings_json_data = HttpInterfaceInfo.objects.all()
        interface_settings_json_list = []
        indexNum = 0
        # 数据库读取数据并插入字典
        for i in interface_settings_json_data.order_by("-interface_id"):
            interface_settings_json_list.append({})
            interface_settings_json_list[indexNum]["interfaceId"] = i.interface_id
            interface_settings_json_list[indexNum]["httpInterface"] = i.http_interface
            interface_settings_json_list[indexNum]["params"] = i.params
            interface_settings_json_list[indexNum]["secretkey"] = i.secretkey
            interface_settings_json_list[indexNum]["interfaceName"] = i.interface_name
            interface_settings_json_list[indexNum]["interfaceCode"] = i.interface_code
            indexNum = indexNum + 1
        paging_object = Paginator(interface_settings_json_list, rows)
        results = paging_object.page(page).object_list
        logger.info("分页结果数据类型为:" + str(type(results)))
        logger.info("分页结束results=" + str(results))
        total_Records = paging_object.count
        interface_settings_json_str = simplejson.dumps({"totalRecord": total_Records, "results": results})
        return HttpResponse(interface_settings_json_str, content_type="application/json")
    except Exception as e:
        logger.error(e)
        logger.exception(u"测试接口设置页面分页错误如下:")


# 功能菜单-测试接口设置数据处理
def interface_setting(request):
    try:
        result = "success!!!"
        # 接收json数据
        if request.method == 'POST':
            received_json_data = request.POST.get("effectRow")
            datalist = simplejson.loads(received_json_data.encode("utf-8"))
            if "inserted" in datalist:
                for i in list(simplejson.loads(datalist["inserted"])):
                    # 增加数据
                    logger.info(received_json_data.encode("utf-8"))
                    http_interface_info_db = HttpInterfaceInfo(http_interface=i["httpInterface"], params=i["params"],
                                                               secretkey=i["secretkey"],
                                                               interface_name=i["interfaceName"],
                                                               interface_code=i["interfaceCode"])
                    http_interface_info_db.save()
            if "deleted" in datalist:
                for i in list(simplejson.loads(datalist["deleted"])):
                    # 删除数据
                    HttpInterfaceInfo.objects.get(interface_id=i["interfaceId"]).delete()
            if "updated" in datalist:
                for i in list(simplejson.loads(datalist["updated"])):
                    # 更新数据
                    HttpInterfaceInfo.objects.filter(interface_id=i["interfaceId"]).update(
                        http_interface=i["httpInterface"], params=i["params"], secretkey=i["secretkey"],
                        interface_name=i["interfaceName"], interface_code=i["interfaceCode"])
            result = simplejson.dumps(result)
            return HttpResponse(result)
        else:
            result = "error!!!"
            result = simplejson.dumps(result)
            return HttpResponse(result)
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")
