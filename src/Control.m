/*
 * Copyright (c) 2016-2017, Grant Paul
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 * 
 * 1. Redistributions of source code must retain the above copyright notice, this
 *    list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
 * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#import "Control.h"

/* Erased generic parameter. */
typedef id ValueType;


@implementation Control

- (instancetype)initWithCenter:(CGVector)center anchor:(CGPoint)anchor size:(CGSize)size slop:(UIEdgeInsets)slop
{
    if (self = [super init]) {
        _center = center;
        _anchor = anchor;
        _size = size;
        _slop = slop;
    }

    return self;
}

@end


@implementation Button

- (instancetype)initWithName:(NSString *)name value:(ValueType)value center:(CGVector)center anchor:(CGPoint)anchor size:(CGSize)size slop:(UIEdgeInsets)slop
{
    if (self = [super initWithCenter:center anchor:anchor size:size slop:slop]) {
        _name = [name copy];
        _value = value;
    }

    return self;
}

@end


@implementation Pad

- (instancetype)initWithUpValue:(ValueType)up leftValue:(ValueType)left downValue:(ValueType)down rightValue:(ValueType)right center:(CGVector)center anchor:(CGPoint)anchor size:(CGSize)size slop:(UIEdgeInsets)slop
{
    if (self = [super initWithCenter:center anchor:anchor size:size slop:slop]) {
        _upValue = up;
        _leftValue = left;
        _downValue = down;
        _rightValue = right;
    }

    return self;
}

@end

