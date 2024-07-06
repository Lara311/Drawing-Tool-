from django.shortcuts import render, redirect
from .models import Shape, Suggestion

def draw_shape(request):
    floor = request.session.get('floor', {'width': 500, 'height': 500, 'color': '#ffffff'})  # Default floor dimensions and color

    if request.method == 'POST':
        shape_width = int(request.POST.get('shape_width'))
        shape_height = int(request.POST.get('shape_height'))
        shape_x = int(request.POST.get('shape_x'))
        shape_y = int(request.POST.get('shape_y'))
        shape_color = request.POST.get('shape_color')
        shape_name = request.POST.get('shape_name')

        if shape_x + shape_width <= floor['width'] and shape_y + shape_height <= floor['height']:
            Shape.objects.create(
                width=shape_width,
                height=shape_height,
                x=shape_x,
                y=shape_y,
                color=shape_color,
                name=shape_name
            )
        return redirect('draw_shape')

    shapes = Shape.objects.all()
    return render(request, 'shapes/draw_shape.html', {'floor': floor, 'shapes': shapes})

def update_floor(request):
    if request.method == 'POST':
        floor_width = int(request.POST.get('floor_width'))
        floor_height = int(request.POST.get('floor_height'))
        floor_color = request.POST.get('floor_color')
        floor = {
            'width': floor_width,
            'height': floor_height,
            'color': floor_color
        }
        request.session['floor'] = floor
        shapes = Shape.objects.all()
        return render(request, 'shapes/draw_shape.html', {'floor': floor, 'shapes': shapes})
    return redirect('draw_shape')

def delete_shape(request):
    if request.method == 'POST':
        shape_id = request.POST.get('shape_id')
        Shape.objects.filter(id=shape_id).delete()
    return redirect('draw_shape')

def home(request):
    return render(request, 'shapes/home.html')

def ideas(request):
    if request.method == 'POST':
        suggestion_text = request.POST.get('suggestion')
        if suggestion_text:
            Suggestion.objects.create(text=suggestion_text)
        return redirect('ideas')

    return render(request, 'shapes/ideas.html')
