% V0 - Initial speed
% α - Initial orientation in space 
% x(t) = v0xt,
% y(t) = v0yt
% V0x = v0 cos(α)
% V0y = v0 sin(α)

function plot_regions(regions, color)
    for i = 1:size(regions, 1)
        x = regions(i, 1:2);
        y = regions(i, 3:4);
        plot(x, y, color, 'LineWidth', 2)
        hold on
    end
end

function [isValid, x_list, y_list] = calcuate_trajectory(v_0x, v_0y, x_0, y_0, allowed_regions, forbidden_regions)
    x_list = [];
    y_list = [];
    t = 0;
    g = 10;
    isValid = true;
    while true
        x = v_0x * t + x_0;
        x_list(end + 1) = x;

        y = v_0y * t - 1/2 * g * t*t + y_0;
        y_list(end + 1) = y;
        if  y < 0
            break
        end
        if validate(x, y, allowed_regions, forbidden_regions)==false
            
        end
        t = t + 0.01;
    end
end

function [isValid] = validate(x, y, allowed, forbidden)
    isValid = true;
end


%% Define allowed and forbidden regios

allowed_regions = [
    4, 7, 1, 1; % x_start, x_end, y_start, y_end
    2, 2, 1, 4; % x_start, x_end, y_start, y_end
];
plot_regions(allowed_regions, 'g');

forbidden_regions = [
    3, 3, 2, 3; % x_start, x_end, y_start, y_end
];
plot_regions(forbidden_regions, 'r');



%% Simulate
x_0 = 0;
y_0 = 5;



for i = 0:1:100
    v_0 = randi(10);
    alpha_deg = randi(90);
    alphe_rad = deg2rad(alpha_deg);
    v_0x = v_0 * cos(alphe_rad);
    v_0y = v_0 * sin(alphe_rad);
    [correct, x, y] = calcuate_trajectory(v_0x, v_0y,x_0, y_0, allowed_regions, forbidden_regions);
    if correct==true
        plot(x, y, 'Color', [rand(), rand() * 0.3, rand()])
        hold on
    end
end


xlim([0, inf]);
ylim([0, inf]);