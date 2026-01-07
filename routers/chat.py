from asyncio import sleep
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from models.chat import ChatCompletionRequest, ChatMessage


router = APIRouter()


async def response_stream_generator():
    sentence = """
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Expedita excepturi neque iure! Voluptatibus obcaecati quod magnam nulla nobis natus recusandae numquam soluta, alias officia nam! Ipsum repudiandae doloribus velit voluptatibus, voluptate voluptatem expedita aut id voluptatum, recusandae animi libero repellat repellendus, cumque similique necessitatibus culpa commodi ad. Quod, fuga totam, molestiae possimus temporibus voluptas laudantium natus quae distinctio quasi delectus sunt, aperiam minus accusantium reprehenderit aspernatur doloribus cum? Necessitatibus laborum, quod incidunt eum maiores, error recusandae culpa dolorum, nihil laboriosam velit est odio consequatur sunt deleniti sed ex ab? In recusandae accusantium laborum incidunt fuga vero iste doloremque consequuntur repellat. Architecto asperiores in inventore? Ratione asperiores nisi repellat eum maiores quaerat velit quia molestiae saepe consectetur incidunt nesciunt fuga, rerum quibusdam omnis exercitationem sapiente consequuntur itaque a! Porro tenetur suscipit incidunt dicta quia dolores. Possimus odit suscipit soluta esse ipsa maiores repellat eos, dolorem molestiae cupiditate quam officia laborum eveniet modi ducimus quisquam quas amet rem corporis recusandae. Dolorem quo, deserunt laboriosam quod repudiandae, corporis est consequatur in, similique eos obcaecati vero rem corrupti esse quidem recusandae minima nihil! Rem nihil tempore est voluptas sapiente molestiae esse quaerat dignissimos iure necessitatibus. Veniam ratione, quos id sequi voluptate architecto, eligendi minima et quaerat doloribus inventore ducimus rerum vel in doloremque. Quae sunt vitae necessitatibus eveniet, accusantium veritatis perferendis odit soluta quibusdam, qui voluptate asperiores nostrum debitis eos quam! Numquam adipisci sunt doloribus repudiandae, natus necessitatibus quas deleniti! Ut iusto laborum, cupiditate fugiat, commodi officia ipsam minima maxime itaque sit blanditiis fuga, qui odit impedit magni. Doloribus ea rerum vel. Facere quidem cumque odio voluptatum amet. Vel, ipsa. Vel, dolor aliquam a dolores quae magni perspiciatis. Delectus totam excepturi illo id qui officiis eos, sequi molestias autem eius.
    """
    for word in sentence.split():
        yield f"event:ayush_bola\ndata: {word}\n\n"
        await sleep(0.2)


# event: <type>
# id: <optional-id>
# data: <payload>
# retry: <ms>


def current_query(self) -> ChatMessage:
    return next(m for m in reversed(self.messages) if m.role == "user")


@router.post("/", response_class=StreamingResponse)
async def chat(chat_completion_request: ChatCompletionRequest):
    print(chat_completion_request.model_dump_json(indent=4))
    print(current_query(chat_completion_request))
    generator = response_stream_generator()
    return StreamingResponse(  # SSE
        generator,
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )


@router.get("/test")
async def chat_test():
    generator = response_stream_generator()
    return StreamingResponse(  # SSE
        generator,
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )
