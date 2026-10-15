alpha_list = [];
v0_list = [];


figure;

for c = 1:100000
    alpha = deg2rad(1 + rand() * (89 - 1));
    v0 = 1 + rand() * (30 - 1);
    
    param_a = (-10) / (2 * v0 * v0 * cos(alpha) * cos(alpha));
    param_b = tan(alpha);
    yc1 = 5 * 5 * param_a + 5 * param_b;
    yc2 = 12 * 12 * param_a + 12 * param_b;
    if (yc1 > 4) && (yc1 < 5)
        continue
    end
    if (yc2 > 4) && (yc2 < 5)
        continue
    end
    
    param_c = -3;
    delta = param_b * param_b - 4 * param_a * param_c;
    
    if (delta > 0)
         sqrt_delta = sqrt(delta);
         x1 = ((-1) * param_b - sqrt_delta) / (2 * param_a);
         x2 = ((-1) * param_b + sqrt_delta) / (2 * param_a);
         
         x_min = min(x1, x2);
         x_max = max(x1, x2);
         
         if ((x_min > 2 && x_min < 8) && (x_max > 9 && x_max < 15))
              alpha_list(end + 1) = alpha;
              v0_list(end + 1) = v0;
              
              y_values = [];
              xx = 0:0.1:18;
              for x_values = 0:0.1:18
                y_values(end+1) = param_a * x_values * x_values + param_b * x_values;
              end
             
              plot(xx, y_values);
              hold on;
           
         end
    end
end
x_v = [2:0.01:8];
y_v = x_v * 0 + 3;
plot(x_v, y_v, 'g');
hold on;
x_v = [9:0.01:15];
y_v = x_v * 0 + 3;
plot(x_v, y_v, 'g');
hold on;
y_v = [4:0.01:5];
x_v = y_v * 0 + 5;
plot(x_v, y_v, 'r');
hold on;
y_v = [4:0.01:5];
x_v = y_v * 0 + 12;
plot(x_v, y_v, 'r');
hold on;


hold off;


plot(alpha_list, v0_list, '.');
xlim([0, max(x)]);
ylim([0, max(y)]);