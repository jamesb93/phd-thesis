Server.killAll();

(
s.waitForBoot({
    b = Buffer.read(s, "/Users/james/dev/webdev/phd-kit/static/ss/gesture.wav");
    s.sync;
    c = Buffer.new(s);

    FluidBufNoveltySlice.process(s, b, threshold:0.45, indices:c, action:{

        c.loadToFloatArray(action:{ | indices | ~indices = indices.as(Array) });

        s.sync;

        ~indices_desc = Array.newClear;

        ~indices.do({ | index, i |
            var color, next_index;
            if(i < (~indices.size - 1), {next_index = ~indices[i+1]}, {next_index = b.numFrames});
            color = Color.rand(0.0, 1.0).hexString;
            ~indices[i] = [index, next_index, color];
            ~indices_desc = ~indices_desc.add((
                start: index,
                end: next_index,
                color: color.asString.quote;
            ));
        });

        ~rand_indices = ~indices.scramble;

        ~final_array  = Array.newClear;
        ~rand_samples = Array.newClear;

        ~rand_indices.do({ | entry |
            var index = entry[0].asInteger;
            var next_index = entry[1].asInteger;
            var color = entry[2];
            b.loadToFloatArray(index, next_index - index, { | samples |
                ~rand_samples = ~rand_samples.add(samples);
            });

            ~final_array = ~final_array.add((
                start: index,
                end: next_index,
                color: color.asString.quote
            ));
        });

        s.sync;

        ~rand_samples = ~rand_samples.flatten;

        d = Buffer.loadCollection(s, ~rand_samples, b.numChannels);

        d.write("~/sage-shuffled.wav".standardizePath,"WAV","float");

        s.sync;

        ~prev = ~final_array[0].start;
        ~length = 0.0;
        ~formatted = Array.newClear;

        ~final_array.do({
            arg slice;
            var len;

            len = slice.end - slice.start;

            ~formatted = ~formatted.add((
                start: ~length,
                end: (~length + len),
                color: slice.color
            ));

            ~length = ~length + len;
        });

        // Write JSON
        // pre
        ~pre = File("~/pre.json".standardizePath, "w");
        ~pre.write("{" + "segments".quote + ": [\n");
        ~indices_desc.do({ |slice, i|
            var str;
            str = slice.asString.replace("(", "{");
            str = str.replace(")", "}");
            str = str.replace("'", '"');
            ~pre.write(str);
            if (i < (~indices_desc.size - 1), { ~pre.write("," ++ "\n") }, { ~pre.write("\n") });

        });
        ~pre.write("] } \n");
        ~pre.close();

        // post
        ~post = File("~/post.json".standardizePath, "w");
        ~post.write("{" + "segments".quote + ": [\n");
        ~formatted.do({ |slice, i|
            var str;
            str = slice.asString.replace("(", "{");
            str = str.replace(")", "}");
            str = str.replace("'", '"');
            ~post.write(str);
            if (i < (~formatted.size - 1), { ~post.write("," ++ "\n") }, { ~post.write("\n") });

        });
        ~post.write("] } \n");
        ~post.close();

    });
});
)