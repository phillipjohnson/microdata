#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import collections

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader('templates'))

def render_str(template, **params):
        t = jinja_environment.get_template(template)
        return t.render(params)

class BaseHandler(webapp2.RequestHandler):
        def render(self, template, **kw):
                self.response.out.write(render_str(template, **kw))

        def write(self, *a, **kw):
                self.response.out.write(*a, **kw)    

class MainHandler(BaseHandler):
    general_params = collections.OrderedDict()
    time_params = collections.OrderedDict()
    nutrition_params = collections.OrderedDict()
    details_params = collections.OrderedDict()
    
    def get(self):
	defaults = dict(cookTime_hide = 'checked',
	    prepTime_hide = 'checked',
	    totalTime_hide = 'checked')
	self.render("form.html",**defaults)
    
    def post(self):
	url = self.request.get('url')
	url_hide = self.request.get('url_hide')
	description = self.request.get('description')
	description_hide = self.request.get('description_hide')
	image = self.request.get('image')
	image_hide = self.request.get('image_hide')
	author = self.request.get('author')
	author_hide = self.request.get('author_hide')
	cookingMethod = self.request.get('cookingMethod')
	cookingMethod_hide = self.request.get('cookingMethod_hide')
	recipeCategory = self.request.get('recipeCategory')
	recipeCategory_hide = self.request.get('recipeCategory_hide')
	recipeCuisine = self.request.get('recipeCuisine')
	recipeCuisine_hide = self.request.get('recipeCuisine_hide')
	prepTimeHours = self.request.get('prepTimeHours')
	prepTimeMinutes = self.request.get('prepTimeMinutes')
	prepTime_hide = self.request.get('prepTime_hide')
	cookTimeHours = self.request.get('cookTimeHours')
	cookTimeMinutes = self.request.get('cookTimeMinutes')
	cookTime_hide = self.request.get('cookTime_hide')
	totalTimeHours = self.request.get('totalTimeHours')
	totalTimeMinutes = self.request.get('totalTimeMinutes')
	totalTime_hide = self.request.get('totalTime_hide')
	recipeYield = self.request.get('recipeYield')
	recipeYield_hide = self.request.get('recipeYield_hide')
	servingSize = self.request.get('servingSize')
	servingSize_hide = self.request.get('servingSize_hide')
	calories = self.request.get('calories')
	calories_hide = self.request.get('calories_hide')
	carbohydrateContent = self.request.get('carbohydrateContent')
	carbohydrateContent_hide = self.request.get('carbohydrateContent_hide')
	fiberContent = self.request.get('fiberContent')
	fiberContent_hide = self.request.get('fiberContent_hide')
	sugarContent = self.request.get('sugarContent')
	sugarContent_hide = self.request.get('sugarContent_hide')
	fatContent = self.request.get('fatContent')
	fatContent_hide = self.request.get('fatContent_hide')
	saturatedFatContent = self.request.get('saturatedFatContent')
	saturatedFatContent_hide = self.request.get('saturatedFatContent_hide')
	unsaturatedFatContent = self.request.get('unsaturatedFatContent')
	unsaturatedFatContent_hide = self.request.get('unsaturatedFatContent_hide')
	transFatContent = self.request.get('transFatContent')
	transFatContent_hide = self.request.get('transFatContent_hide')
	cholesterolContent = self.request.get('cholesterolContent')
	cholesterolContent_hide = self.request.get('cholesterolContent_hide')
	proteinContent = self.request.get('proteinContent')
	proteinContent_hide = self.request.get('proteinContent_hide')
	sodiumContent = self.request.get('sodiumContent')
	sodiumContent_hide = self.request.get('sodiumContent_hide')
	ingredients = self.request.get('ingredients')
	ingredients_hide = self.request.get('ingredients_hide')
	instructions = self.request.get('instructions')
	instructions_hide = self.request.get('instructions_hide')
	keywords = self.request.get('keywords')
	keywords_hide = self.request.get('keywords_hide')
	
	self.general_params['url'] = url
	self.general_params['url_hide'] = url_hide
	self.general_params['description'] = description
	self.general_params['description_hide'] = description_hide
	self.general_params['image'] = image
	self.general_params['image_hide'] = image_hide
	self.general_params['author'] = author
	self.general_params['author_hide'] = author_hide
	self.general_params['cookingMethod'] = cookingMethod
	self.general_params['cookingMethod_hide'] = cookingMethod_hide
	self.general_params['recipeCategory'] = recipeCategory
	self.general_params['recipeCategory_hide'] = recipeCategory_hide
	self.general_params['recipeCuisine'] = recipeCuisine
	self.general_params['recipeCuisine_hide'] = recipeCuisine_hide
	self.general_params['recipeYield'] = recipeYield
	self.general_params['recipeYield_hide'] = recipeYield_hide

	self.time_params['prepTimeHours'] = prepTimeHours
	self.time_params['prepTimeMinutes'] = prepTimeMinutes
	self.time_params['prepTime_hide'] = prepTime_hide
	self.time_params['cookTimeHours'] = cookTimeHours
	self.time_params['cookTimeMinutes'] = cookTimeMinutes
	self.time_params['cookTime_hide'] = cookTime_hide
	self.time_params['totalTimeHours'] = totalTimeHours
	self.time_params['totalTimeMinutes'] = totalTimeMinutes
	self.time_params['totalTime_hide'] = totalTime_hide
	
	self.nutrition_params['servingSize'] = servingSize
	self.nutrition_params['servingSize_hide'] = servingSize_hide
	self.nutrition_params['calories'] = calories
	self.nutrition_params['calories_hide'] = calories_hide
	self.nutrition_params['carbohydrateContent'] = carbohydrateContent
	self.nutrition_params['carbohydrateContent_hide'] = carbohydrateContent_hide
	self.nutrition_params['fiberContent'] = fiberContent
	self.nutrition_params['fiberContent_hide'] = fiberContent_hide
	self.nutrition_params['sugarContent'] = sugarContent
	self.nutrition_params['sugarContent_hide'] = sugarContent_hide
	self.nutrition_params['fatContent'] = fatContent
	self.nutrition_params['fatContent_hide'] = fatContent_hide
	self.nutrition_params['saturatedFatContent'] = saturatedFatContent
	self.nutrition_params['saturatedFatContent_hide'] = saturatedFatContent_hide
	self.nutrition_params['unsaturatedFatContent'] = unsaturatedFatContent
	self.nutrition_params['unsaturatedFatContent_hide'] = unsaturatedFatContent_hide
	self.nutrition_params['transFatContent'] = transFatContent
	self.nutrition_params['transFatContent_hide'] = transFatContent_hide
	self.nutrition_params['cholesterolContent'] = cholesterolContent
	self.nutrition_params['cholesterolContent_hide'] = cholesterolContent_hide
	self.nutrition_params['proteinContent'] = proteinContent
	self.nutrition_params['proteinContent_hide'] = proteinContent_hide
	self.nutrition_params['sodiumContent'] = sodiumContent
	self.nutrition_params['sodiumContent_hide'] = sodiumContent_hide

	self.details_params['ingredients'] = ingredients
	self.details_params['ingredients_hide'] = ingredients_hide
	self.details_params['instructions'] = instructions
	self.details_params['instructions_hide'] = instructions_hide
	self.details_params['keywords'] = keywords
	self.details_params['keywords_hide'] = keywords_hide
	

	
	output = self.generate()
	
	params = {}
	params.update(self.general_params)
	params.update(self.time_params)
	params.update(self.nutrition_params)
	params.update(self.details_params)
	
	params["output"] = output
	
	self.render("form.html",**params)

    def isoifyTimes(self):
	if self.time_params['prepTimeHours'] or self.time_params['prepTimeMinutes']:
	    prepTime='PT'
	    if self.time_params['prepTimeHours']:
		prepTime = prepTime + self.time_params['prepTimeHours'] + 'H'
	    if self.time_params['prepTimeMinutes']:
		prepTime = prepTime + self.time_params['prepTimeMinutes'] + 'M'
	    self.general_params['prepTime'] = prepTime
	    self.general_params['prepTime_hide'] = self.time_params['prepTime_hide']
	    del self.time_params['prepTime_hide']
	if self.time_params['cookTimeHours'] or self.time_params['cookTimeMinutes']:
	    cookTime='PT'
	    if self.time_params['cookTimeHours']:
		cookTime = cookTime + self.time_params['cookTimeHours'] + 'H'
	    if self.time_params['cookTimeMinutes']:
		cookTime = cookTime + self.time_params['cookTimeMinutes'] + 'M'
	    self.general_params['cookTime'] = cookTime
	    self.general_params['cookTime_hide'] = self.time_params['cookTime_hide']
	    del self.time_params['cookTime_hide']
	if self.time_params['totalTimeHours'] or self.time_params['totalTimeMinutes']:
	    totalTime='PT'
	    if self.time_params['totalTimeHours']:
		totalTime = totalTime + self.time_params['totalTimeHours'] + 'H'
	    if self.time_params['totalTimeMinutes']:
		totalTime = totalTime + self.time_params['totalTimeMinutes'] + 'M'
	    self.general_params['totalTime'] = totalTime
	    self.general_params['totalTime_hide'] = self.time_params['totalTime_hide']
	    del self.time_params['totalTime_hide']
    
    def generate(self):
	output = '<div itemscope itemtype="http://schema.org/Recipe">\n<p>\n'
	
	self.isoifyTimes()
	
	output = output + self.formatDictionary(self.general_params) + '\n</p>'
	
	printNutrition = False
	for v in self.nutrition_params.values():
	    if v:
		printNutrition = True
	
	if printNutrition:
	    output = output + '\n<div itemprop="nutrition" itemscope itemtype="http://schema.org/NutritionInformation">\n<p>\n'
	    output = output + self.formatDictionary(self.nutrition_params)
	    output = output + '</p>\n</div>\n'
	
	output = output + '<p>\n' + self.formatDictionary(self.details_params) + '</p>'
	
	output = output + '\n</div>'
	
	output.replace('<','&lt;')
	output.replace('>','&gt;')
	
	return output
	
    def formatDictionary(self,myDict):
	#Update the so that "on" is "checked"
	for k,v in myDict.iteritems():
	    if "_hide" in k:
		if v == u'on':
		    myDict[k] = 'checked'
		    print k
		    print myDict[k]
		
	#Make it purdy
	output = ""
	for k,v in myDict.iteritems():
	    if '_hide' in k: #Ignore the "_hide"
		next
	    elif v:
		hide_key_name = k + '_hide'
		
		if myDict.has_key(hide_key_name):
		    if myDict[k + '_hide'] == 'checked':
			output = output + '<meta itemprop="' + k + '" content="' + v + '">\n'
		    elif k == 'image':
			output = output + '<img itemprop="image" src="' + v + '" /></br>'
		    elif k == 'ingredients':
			ingredients = v.split('\r\n')
			for ingredient in ingredients:
			    ingredient.replace('\r','')
			    output = output + '<span itemprop="' + k + '">' + ingredient + '</span></br>\n'
		    else:
			output = output + '<span itemprop="' + k + '">' + v + '</span></br>\n'
		else:
		    output = output + '<span itemprop="' + k + '">' + v + '</span></br>\n'

    
	return output
            

            
            
app = webapp2.WSGIApplication([
        ('/microdata', MainHandler)
], debug=True)
