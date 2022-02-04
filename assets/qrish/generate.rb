15.times do |x|
  15.times do |y|
    color=['black','white'].sample
    puts "\\fill[color=#{color}] (#{x},#{y}) rectangle (#{x+1},#{y+1});"
  end
end

