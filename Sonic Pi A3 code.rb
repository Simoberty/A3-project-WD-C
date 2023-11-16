
up = "sample :drum_heavy_kick"
down = "sample :drum_snare_hard"
left = "sample :drum_cymbal_closed"
right = "sample :drum_cymbal_open"

live_loop :osPlay0 do
  sync "/live_loop/osPlay0"
  cue:play0 if (nv[0] == 0) #if OSC play[0] play cue
  sample :drum_snare_hard if (nv[0] == 1) #if OSC play[1]
end

live_loop :ply0 do
  sync:play0
  sample :drum_heavy_kick
end

live_loop :osPlay0 do
  sync "/live_loop/osPlay0"
  cue:play0 if (nv[1] == 1) #if OSC play[1] play cue
  sample :drum_cymbal_closed if (nv[1] == 2) #if OSC play[1]
end

live_loop :ply0 do
  sync:play0
  sample :drum_cymbal_open
end


