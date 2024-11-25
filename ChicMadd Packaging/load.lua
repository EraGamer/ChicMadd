local HttpService = game:GetService("HttpService")
local Players = game:GetService("Players")

local response = syn.request({
	Url = ("https://ChicMadd.ethanwaike.repl.co/api/get?gameId=%i&placeId=%i&userId=%i"):format(
		game.GameId,
		game.PlaceId,
		Players.LocalPlayer.UserId
	),
	Method = "GET",
})

if response.Success then
    local Body = HttpService:JSONDecode(response.Body)

	print(Body.whitelisted)
    print(Body.settings)
	loadstring(Body.contents)
else
    print("Failure")
end
