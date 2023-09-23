local request = require "http.request";
local cjson = require "cjson";

local requestURI = request.new_from_uri("http://vid.puffyan.us/api/v1/channels/CHANNEL_ID?fields=latestVideos")

local _, stream = assert(requestURI:go());

local response = assert(stream:get_body_as_string())
local data = cjson.decode(response)

local i = 1

while true do
    local video = data.latestVideos[i]

    if video ~= nil then
        print(video.title)
        i = i + 1
    else
        break
    end
end

print("\nTotal: "..(i - 1).." videos.")
