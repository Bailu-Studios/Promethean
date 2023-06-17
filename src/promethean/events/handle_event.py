import re

from fastapi.responses import JSONResponse

from promethean.api.vila.abc_bot import ABCBot
from promethean.events.audit_callback_event import AuditCallbackEvent
from promethean.events.create_robot_event import CreateRobotEvent
from promethean.events.delete_robot_event import DeleteRobotEvent
from promethean.events.member_add_quick_emoticon_event import MemberAddQuickEmoticonEvent
from promethean.events.member_send_message_event import MemberSendMessageEvent
from promethean.events.new_member_join_event import NewMemberJoinEvent
from promethean.log import logger
from promethean.utils.message import TextMessage


async def handle_event(bot: ABCBot, data: dict) -> JSONResponse:
    if not (payload_data := data.get("event", None)):
        msg = re.sub(r"</?((?:[fb]g\s)?[^<>\s]*)>", r"\\\g<0>", str(data))
        logger.warning(f'Received invalid data: {msg}')
        return JSONResponse(
            status_code=400, content={"retcode": -1, "msg": "Invalid data"}
        )
    event_data: dict = payload_data['extend_data']['EventData']
    if 'JoinVilla' in event_data.keys():
        context = event_data['JoinVilla']
        bot.post_event(NewMemberJoinEvent(
            join_uid=context['join_uid'],
            join_user_nickname=context['join_user_nickname'],
            join_at=context['join_at'],
            villa_id=context['villa_id']
        ))
    if 'SendMessage' in event_data.keys():
        context = event_data['SendMessage']
        bot.post_event(MemberSendMessageEvent(
            TextMessage(
                bot=bot,
                msg_id=context['msg_uid'],
                text=context['content'],
                sender=context['from_user_id'],
                send_time=context['send_at'],
                room_id=context['room_id'],
                villa_id=context['villa_id']
            )
        ))
    if 'CreateRobot' in event_data.keys():
        context = event_data['CreateRobot']
        bot.post_event(CreateRobotEvent(villa_id=context['villa_id']))
    if 'DeleteRobot' in event_data.keys():
        context = event_data['DeleteRobot']
        bot.post_event(DeleteRobotEvent(villa_id=context['villa_id']))
    if 'AddQuickEmoticon' in event_data.keys():
        context = event_data['AddQuickEmoticon']
        bot.post_event(AuditCallbackEvent(
            villa_id=context['villa_id'],
            room_id=context['room_id'],
            uid=context['uid'],
            emoticon_id=context['emoticon_id'],
            emoticon=context['emoticon'],
            msg_uid=context['msg_uid'],
            bot_msg_id=context['bot_msg_id'],
            is_cancel=context['is_cancel']
        ))
    if 'AuditCallback' in event_data.keys():
        context = event_data['AuditCallback']
        bot.post_event(MemberAddQuickEmoticonEvent(
            audit_id=context['audit_id'],
            bot_tpl_id=context['bot_tpl_id'],
            villa_id=context['villa_id'],
            room_id=context['room_id'],
            user_id=context['user_id'],
            pass_through=context['pass_through'],
            audit_result=context['audit_result']
        ))
    return JSONResponse(
        status_code=200, content={"retcode": 0, "msg": "OK"}
    )
