#!/usr/bin/env python

GLOBAL_HEADER = """-------------------------------------------------------------------------------
-- Lua global variables.
-- The basic library provides some core functions to Lua.
-- All the preloaded module of Lua are declared here.
-- @module global
"""

GLOBAL_MODULES = """------------------------------------------------------------------------------
-- This library provides generic functions for coroutine manipulation.
-- This is a global variable which hold the preloaded @{coroutine} module.
-- @field[parent = #global] coroutine#coroutine coroutine preloaded module

------------------------------------------------------------------------------
-- The package library provides basic facilities for loading and building modules in Lua.
-- This is a global variable which hold the preloaded @{package} module.
-- @field[parent = #global] package#package package preloaded module

------------------------------------------------------------------------------
-- This library provides generic functions for string manipulation.
-- This is a global variable which hold the preloaded @{string} module.
-- @field[parent = #global] string#string string preloaded module

------------------------------------------------------------------------------
-- This library provides generic functions for table manipulation.
-- This is a global variable which hold the preloaded @{table} module.
-- @field[parent = #global] table#table table preloaded module

------------------------------------------------------------------------------
-- This library is an interface to the standard C math library.
-- This is a global variable which hold the preloaded @{math} module.
-- @field[parent = #global] math#math math preloaded module

------------------------------------------------------------------------------
-- The I/O library provides function for file manipulation.
-- This is a global variable which hold the preloaded @{io} module.
-- @field[parent = #global] io#io io preloaded module

------------------------------------------------------------------------------
-- Operating System Facilities.
-- This is a global variable which hold the preloaded @{os} module.
-- @field[parent = #global] os#os os preloaded module

------------------------------------------------------------------------------
-- The Debug Library.
-- This is a  global variable which hold the preloaded @{debug} module.
-- @field[parent = #global] debug#debug debug preloaded module

-------------------------------------------------------------------------------
-- Issues an error when the value of its argument `v` is false (i.e.,
-- **nil** or **false**); otherwise, returns all its arguments. `message` is an error
-- message; when absent, it defaults to *"assertion failed!"*.
-- @function [parent=#global] assert
-- @param v if this argument is false an error is issued.
-- @param #string message an error message. defaults value is *"assertion failed"*.
-- @return All its arguments.

-------------------------------------------------------------------------------
-- This function is a generic interface to the garbage collector.
-- It performs different functions according to its first argument, `opt`:
--
--   * **"stop":** stops the garbage collector.
--   * **"restart":** restarts the garbage collector.
--   * **"collect":** performs a full garbage-collection cycle.
--   * **"count":** returns the total memory in use by Lua (in Kbytes).
--   * **"step":** performs a garbage-collection step. The step "size" is controlled
--       by `arg` (larger values mean more steps) in a non-specified way. If you
--       want to control the step size you must experimentally tune the value of
--      `arg`. Returns true if the step finished a collection cycle.
--   * **"setpause":** sets `arg` as the new value for the *pause* of the collector.
--       Returns the previous value for *pause*.
--   * **"setstepmul":** sets `arg` as the new value for the *step multiplier*
--       of the collector. Returns the previous value for *step*.
-- @function [parent=#global] collectgarbage
-- @param #string opt the command to send.
-- @param arg the argument of the command. (optional)

-------------------------------------------------------------------------------
-- Opens the named file and executes its contents as a Lua chunk. When
-- called without arguments,
-- `dofile` executes the contents of the standard input (`stdin`). Returns
-- all values returned by the chunk. In case of errors, `dofile` propagates
-- the error to its caller (that is, `dofile` does not run in protected mode).
-- @function [parent=#global] dofile
-- @param #string filename the path to the file. (optional)

-------------------------------------------------------------------------------
-- Terminates the last protected function called and returns `message`
-- as the error message. Function `error` never returns.
--
-- Usually, `error` adds some information about the error position at the
-- beginning of the message. The `level` argument specifies how to get the
-- error position.
-- With level 1 (the default), the error position is where the
-- `error` function was called.
-- Level 2 points the error to where the function
-- that called `error` was called; and so on.
-- Passing a level 0 avoids the addition of error position information to the message.
-- @function [parent=#global] error
-- @param #string message an error message.
-- @param #number level specifies how to get the error position, default value is `1`.

-------------------------------------------------------------------------------
-- A global variable (not a function) that holds the global environment
-- (that is, `_G._G = _G`). Lua itself does not use this variable; changing
-- its value does not affect any environment, nor vice-versa. (Use `setfenv`
-- to change environments.)
-- @field [parent = #global] #table _G

-------------------------------------------------------------------------------
-- Returns the current environment in use by the function.
-- @function [parent=#global] getfenv
-- @param f can be a Lua function or a number that specifies the function at that
-- stack level: Level 1 is the function calling `getfenv`. If the given
-- function is not a Lua function, or if `f` is `0`, `getfenv` returns the
-- global environment. The default for `f` is `1`.

-------------------------------------------------------------------------------
-- If `object` does not have a metatable, returns nil. Otherwise, if the
-- object's metatable has a `"__metatable"` field, returns the associated
-- value. Otherwise, returns the metatable of the given object.
-- @function [parent=#global] getmetatable
-- @param object
-- @return #table the metatable of object.

-------------------------------------------------------------------------------
-- Use to iterate over a table by index.
-- Returns three values: an iterator function, the table `t`, and 0,
-- so that the construction :
--
--     for i,v in ipairs(t) do *body* end
-- will iterate over the pairs (`1,t[1]`), (`2,t[2]`), ..., up to the
-- first integer key absent from the table.
-- @function [parent=#global] ipairs
-- @param #table t a table by index.

-------------------------------------------------------------------------------
-- Loads a chunk using function `func` to get its pieces. Each call to
-- `func` must return a string that concatenates with previous results. A
-- return of an empty string, **nil,** or no value signals the end of the chunk.
--
-- If there are no errors, returns the compiled chunk as a function; otherwise,
-- returns nil plus the error message. The environment of the returned function
-- is the global environment.
--
-- `chunkname` is used as the chunk name for error messages and debug
-- information. When absent, it defaults to "`=(load)`".
-- @function [parent=#global] load
-- @param func function which loads the chunk.
-- @param #string chunkname chunk name used for error messages and debug information, default value is "`=(load)`".

-------------------------------------------------------------------------------
-- Similar to `load`, but gets the chunk from file `filename` or from the
-- standard input, if no file name is given.
-- @function [parent=#global] loadfile
-- @param #string filename the path to the file. (optional)

-------------------------------------------------------------------------------
-- Similar to `load`, but gets the chunk from the given string.
-- To load and run a given string, use the idiom
--
--     assert(loadstring(s))()
-- When absent, `chunkname` defaults to the given string.
-- @function [parent=#global] loadstring
-- @param #string string lua code to load.
-- @param #string chunkname chunk name used for error messages and debug information, default value is the given string.

-------------------------------------------------------------------------------
-- Allows a program to traverse all fields of a table. Its first argument is
-- a table and its second argument is an index in this table. `next` returns
-- the next index of the table and its associated value.
--
-- When called with nil
-- as its second argument, `next` returns an initial index and its associated
-- value. When called with the last index, or with nil in an empty table, `next`
-- returns nil.
--
-- If the second argument is absent, then it is interpreted as
-- nil. In particular, you can use `next(t)` to check whether a table is empty.
-- The order in which the indices are enumerated is not specified, *even for
-- numeric indices*. (To traverse a table in numeric order, use a numerical
-- for or the `ipairs` function.)
--
-- The behavior of `next` is *undefined* if, during the traversal, you assign
-- any value to a non-existent field in the table. You may however modify
-- existing fields. In particular, you may clear existing fields.
-- @function [parent=#global] next
-- @param #table table table to traverse.
-- @param index initial index.

-------------------------------------------------------------------------------
-- Use to iterate over a table.
-- Returns three values: the `next` function, the table `t`, and nil,
-- so that the construction :
--
--     for k,v in pairs(t) do *body* end
-- will iterate over all key-value pairs of table `t`.
--
-- See function `next` for the caveats of modifying the table during its
-- traversal.
-- @function [parent=#global] pairs
-- @param #table t table to traverse.

-------------------------------------------------------------------------------
-- Calls function `f` with the given arguments in *protected mode*. This
-- means that any error inside `f` is not propagated; instead, `pcall` catches
-- the error and returns a status code. Its first result is the status code (a
-- boolean), which is true if the call succeeds without errors. In such case,
-- `pcall` also returns all results from the call, after this first result. In
-- case of any error, `pcall` returns false plus the error message.
-- @function [parent=#global] pcall
-- @param f function to be call in *protected mode*.
-- @param ... function arguments.
-- @return #boolean true plus the result of `f` function if its call succeeds without errors.
-- @return #boolean,#string  false plus the error message in case of any error.

-------------------------------------------------------------------------------
-- Receives any number of arguments, and prints their values to `stdout`,
-- using the `tostring` function to convert them to strings. `print` is not
-- intended for formatted output, but only as a quick way to show a value,
-- typically for debugging. For formatted output, use `string.format`.
-- @function [parent=#global] print
-- @param ... values to print to `stdout`.

-------------------------------------------------------------------------------
-- Checks whether `v1` is equal to `v2`, without invoking any
-- metamethod. Returns a boolean.
-- @function [parent=#global] rawequal
-- @param v1
-- @param v2
-- @return #boolean true if `v1` is equal to `v2`.

-------------------------------------------------------------------------------
-- Gets the real value of `table[index]`, without invoking any
-- metamethod. `table` must be a table; `index` may be any value.
-- @function [parent=#global] rawget
-- @param #table table
-- @param index may be any value.
-- @return The real value of `table[index]`, without invoking any
-- metamethod.

-------------------------------------------------------------------------------
-- Sets the real value of `table[index]` to `value`, without invoking any
-- metamethod. `table` must be a table, `index` any value different from nil,
-- and `value` any Lua value.
-- This function returns `table`.
-- @function [parent=#global] rawset
-- @param #table table
-- @param index any value different from nil.
-- @param value any Lua value.

-------------------------------------------------------------------------------
-- If `index` is a number, returns all arguments after argument number
-- `index`. Otherwise, `index` must be the string `"#"`, and `select` returns
-- the total number of extra arguments it received.
-- @function [parent=#global] select
-- @param index a number or the string `"#"`
-- @param ...

-------------------------------------------------------------------------------
-- Sets the environment to be used by the given function. `f` can be a Lua
-- function or a number that specifies the function at that stack level: Level
-- 1 is the function calling `setfenv`. `setfenv` returns the given function.
-- As a special case, when `f` is 0 `setfenv` changes the environment of the
-- running thread. In this case, `setfenv` returns no values.
-- @function [parent=#global] setfenv
-- @param f a Lua function or a number that specifies the stack level.
-- @param #table table used as environment for `f`.
-- @return The given function.

-------------------------------------------------------------------------------
-- Sets the metatable for the given table. (You cannot change the metatable
-- of other types from Lua, only from C.) If `metatable` is nil, removes the
-- metatable of the given table. If the original metatable has a `"__metatable"`
-- field, raises an error.
-- This function returns `table`.
-- @function [parent=#global] setmetatable
-- @param #table table
-- @param #table metatable
-- @return The first argument `table`.

-------------------------------------------------------------------------------
-- Tries to convert its argument to a number. If the argument is already
-- a number or a string convertible to a number, then `tonumber` returns this
-- number; otherwise, it returns **nil.**
--
-- An optional argument specifies the base to interpret the numeral. The base
-- may be any integer between 2 and 36, inclusive. In bases above 10, the
-- letter '`A`' (in either upper or lower case) represents 10, '`B`' represents
-- 11, and so forth, with '`Z`' representing 35. In base 10 (the default),
-- the number can have a decimal part, as well as an optional exponent part.
-- In other bases, only unsigned integers are accepted.
-- @function [parent=#global] tonumber
-- @param e a number or string to convert to a number.
-- @param #number base the base to interpret the numeral, any integer between 2 and 36.(default is 10).
-- @return #number a number if conversion succeeds else **nil**.

-------------------------------------------------------------------------------
-- Receives an argument of any type and converts it to a string in a
-- reasonable format. For complete control of how numbers are converted, use
-- `string.format`.
--
-- If the metatable of `e` has a `"__tostring"` field, then `tostring` calls
-- the corresponding value with `e` as argument, and uses the result of the
-- call as its result.
-- @function [parent=#global] tostring
-- @param e an argument of any type.
-- @return #string a string in a reasonable format.

-------------------------------------------------------------------------------
-- Returns the type of its only argument, coded as a string. The possible
-- results of this function are "
-- `nil`" (a string, not the value nil), "`number`", "`string`", "`boolean`",
-- "`table`", "`function`", "`thread`", and "`userdata`".
-- @function [parent=#global] type
-- @param v any value.
-- @return #string the type of `v`.

-------------------------------------------------------------------------------
-- Returns the elements from the given table. This function is equivalent to
--
--     return list[i], list[i+1], ..., list[j]
-- except that the above code can be written only for a fixed number of
-- elements. By default, `i` is 1 and `j` is the length of the list, as
-- defined by the length operator.
-- @function [parent=#global] unpack
-- @param #table list a table by index
-- @param i index of first value.
-- @param j index of last value.

-------------------------------------------------------------------------------
-- A global variable (not a function) that holds a string containing the
-- current interpreter version. The current contents of this variable is
-- "`Lua 5.1`".
-- @field [parent = #global] #string _VERSION

-------------------------------------------------------------------------------
-- This function is similar to `pcall`, except that you can set a new
-- error handler.
--
-- `xpcall` calls function `f` in protected mode, using `err` as the error
-- handler. Any error inside `f` is not propagated; instead, `xpcall` catches
-- the error, calls the `err` function with the original error object, and
-- returns a status code. Its first result is the status code (a boolean),
-- which is true if the call succeeds without errors. In this case, `xpcall`
-- also returns all results from the call, after this first result. In case
-- of any error, `xpcall` returns false plus the result from `err`.
-- @function [parent=#global] xpcall
-- @param f function to be call in *protected mode*.
-- @param err function used as error handler.
-- @return #boolean true plus the result of `f` function if its call succeeds without errors.
-- @return #boolean,#string  false plus the result of `err` function.

-------------------------------------------------------------------------------
-- Creates a module. If there is a table in `package.loaded[name]`,
-- this table is the module. Otherwise, if there is a global table `t`
-- with the given name, this table is the module.
--
-- Otherwise creates a new table `t` and sets it as the value of the global
-- `name` and the value of `package.loaded[name]`.
--  This function also initializes `t._NAME` with the
-- given name, `t._M` with the module (`t` itself), and `t._PACKAGE` with the
-- package name (the full module name minus last component; see below). Finally,
-- `module` sets `t` as the new environment of the current function and the
-- new value of `package.loaded[name]`, so that `require` returns `t`.
--
-- If `name` is a compound name (that is, one with components separated by
-- dots), `module` creates (or reuses, if they already exist) tables for each
-- component. For instance, if `name` is `a.b.c`, then `module` stores the
-- module table in field `c` of field `b` of global `a`.
--
-- This function can receive optional *options* after the module name, where
-- each option is a function to be applied over the module.
-- @function [parent=#global] module
-- @param name the module name.

-------------------------------------------------------------------------------
-- Loads the given module. The function starts by looking into the
-- `package.loaded` table to determine whether `modname` is already
-- loaded. If it is, then `require` returns the value stored at
-- `package.loaded[modname]`. Otherwise, it tries to find a *loader* for
-- the module.
--
-- To find a loader, `require` is guided by the `package.loaders` array. By
-- changing this array, we can change how `require` looks for a module. The
-- following explanation is based on the default configuration for
-- `package.loaders`.
--
-- First `require` queries `package.preload[modname]`. If it has a value,
-- this value (which should be a function) is the loader. Otherwise `require`
-- searches for a Lua loader using the path stored in `package.path`. If
-- that also fails, it searches for a C loader using the path stored in
-- `package.cpath`. If that also fails, it tries an *all-in-one* loader (see
-- `package.loaders`).
--
-- Once a loader is found, `require` calls the loader with a single argument,
-- `modname`. If the loader returns any value, `require` assigns the returned
-- value to `package.loaded[modname]`. If the loader returns no value and
-- has not assigned any value to `package.loaded[modname]`, then `require`
-- assigns true to this entry. In any case, `require` returns the final value
-- of `package.loaded[modname]`.
--
-- If there is any error loading or running the module, or if it cannot find
-- any loader for the module, then `require` signals an error.
-- @function [parent=#global] require
-- @param #string modname name of module to load.

return nil
"""

ROCKSPEC = """package = "defold"
version = "${DEFOLD_VERSION}"
grammar = "lua-5.1"
flags = { ee = true }
description = {
	summary = "Defold Execution Environment",
	detailed = [[ Defold Execution Environment Support]],
	licence = "?",
	homepage= "http://www.defold.com"
}
api = {
	file = "${API_ZIP}"
}
documentation = {}
"""


import os
import re
import sqlite3
import shutil
import urllib
import urllib2
import json
import zipfile
import string
from subprocess import call


# path definitions
EXTRACT_PATH = "extract"
DEFOLD_API_PATH = os.path.join(EXTRACT_PATH, "api")
LUA_API_PATH = os.path.join("resources", "api")

API_ZIP = "api.zip"
ROCKSPEC_FILE = "defold.rockspec"
REF_DOC_ZIP = "ref-doc.zip"
REF_DOC_JSON_PATH = "json"


def get_defold_sha1():
	info_url = "http://d.defold.com/stable/info.json"
	info_file = urllib.urlopen(info_url)
	info = json.loads(info_file.read())
	info_file.close()
	return info["sha1"]

def get_defold_version():
	info_url = "http://d.defold.com/stable/info.json"
	info_file = urllib.urlopen(info_url)
	info = json.loads(info_file.read())
	info_file.close()
	return info["version"]

def get_ref_doc():
	print("Downloading ref-doc.zip")
	sha1 = get_defold_sha1()
	if os.path.exists(REF_DOC_ZIP):
		os.remove(REF_DOC_ZIP)
	urllib.urlretrieve("http://d.defold.com/archive/" + sha1 + "/engine/share/ref-doc.zip", REF_DOC_ZIP)

def unzip_ref_doc():
	print("Unpacking ref-doc.zip")
	if os.path.exists(REF_DOC_JSON_PATH):
		shutil.rmtree(REF_DOC_JSON_PATH)

	with zipfile.ZipFile(REF_DOC_ZIP) as zf:
		zf.extractall(REF_DOC_JSON_PATH)

def create_api():
	if os.path.exists(EXTRACT_PATH):
		shutil.rmtree(EXTRACT_PATH)
		
	os.makedirs(DEFOLD_API_PATH)

	global_doc = GLOBAL_HEADER + "\n"
	
	for root, dir, files in os.walk(REF_DOC_JSON_PATH):
		for file in files:
			with open(os.path.join(root, file), "r") as fh:
				if file.endswith(".json"):
					print("  Parsing " + file)
					class_name = file.replace("_doc.json", "")
					global_doc = global_doc + "---\n"
					global_doc = global_doc + "-- @field[parent = #global] " + class_name + "#" + class_name + " " + class_name + "\n\n"
					class_doc = "---\n"
					class_doc = "-- @module " + class_name + "\n\n\n\n"
					for element in json.load(fh)["elements"]:
						element_name = element["name"]
						if element_name != "":
							entry_type = "Function"
							if element["type"] == "VARIABLE":
								class_doc = class_doc + "---\n"
								class_doc = class_doc + "-- @field [parent=#" + class_name + "] " + element_name + "\n"
							elif element["type"] == "MESSAGE":
								class_doc = class_doc + "---\n"
								class_doc = class_doc + "-- @field [parent=#" + class_name + "] " + element_name + "\n"
							elif element["type"] == "PROPERTY":
								class_doc = class_doc + "---\n"
								class_doc = class_doc + "-- @field [parent=#" + class_name + "] " + element_name + "\n"
							else:
								class_doc = class_doc + "---\n"
								class_doc = class_doc + "-- @function [parent=#" + class_name + "] " + element_name + "\n"
					
							class_doc = class_doc + "-- " + element["brief"] + "\n"
							if element["description"] != "":
								class_doc = class_doc + "-- " + element["description"].replace("\n", "\n-- ") + "\n"
							if len(element["parameters"]) > 0:
								for parameter in element["parameters"]:
									class_doc = class_doc + "-- @param " + parameter["name"] + " "  + parameter["doc"] + "\n"
							if len(element["returnvalues"]) > 0:
								for returnvalue in element["returnvalues"]:
									class_doc = class_doc + "-- @return" + returnvalue["name"] + " " + returnvalue["doc"] + "\n"
							if element["examples"] != "":
								class_doc = class_doc + "-- @usage" + element["examples"].replace("\n", "\n-- ") + "\n"

							class_doc = class_doc + "\n\n"
					
					with open(os.path.join(DEFOLD_API_PATH, class_name + ".doclua"), "w") as out:
						out.write(class_doc)

		
		global_doc = global_doc + GLOBAL_MODULES
		with open(os.path.join(DEFOLD_API_PATH, "global.doclua"), "w") as out:
			out.write(global_doc)

def create_rockspec():
	with open(ROCKSPEC_FILE, "w") as out:
		out.write(string.Template(ROCKSPEC).substitute({ "DEFOLD_VERSION": get_defold_version(), "API_ZIP": API_ZIP }))

def create_archive():
	if os.path.exists(API_ZIP):
		os.remove(API_ZIP)

	zipf = zipfile.ZipFile(API_ZIP, 'w', zipfile.ZIP_DEFLATED)
	for root, dirs, files in os.walk(DEFOLD_API_PATH):
		for file in files:
			zipf.write(os.path.join(root, file), file)
	for root, dirs, files in os.walk(LUA_API_PATH):
		for file in files:
			zipf.write(os.path.join(root, file), file)
	zipf.close()

	zipf = zipfile.ZipFile("defold-ldt.zip", 'w', zipfile.ZIP_DEFLATED)
	zipf.write(API_ZIP)
	zipf.write(ROCKSPEC_FILE)
	zipf.close()
	
def cleanup():
	print("Performing cleanup")
	if os.path.exists(REF_DOC_JSON_PATH):
		shutil.rmtree(REF_DOC_JSON_PATH)
	if os.path.exists(EXTRACT_PATH):
		shutil.rmtree(EXTRACT_PATH)
	if os.path.exists(REF_DOC_ZIP):
		os.remove(REF_DOC_ZIP)
	if os.path.exists(API_ZIP):
		os.remove(API_ZIP)
	if os.path.exists(ROCKSPEC_FILE):
		os.remove(ROCKSPEC_FILE)


get_ref_doc()
unzip_ref_doc()
create_api()
create_rockspec()
create_archive()
cleanup()
